#!/usr/bin/env python3
"""
Restore lost metadata fields from the main branch into current YAML files.

For each YAML file that exists in both main and the current branch,
this script checks if the main branch version had values for:
  release_date, website, tags, access, region, name_en

If the current file is missing any of these fields, they are restored
from main (only if the main version had them).
"""

import subprocess
import sys
import os
import yaml

# Fields to restore from main if missing in current
FIELDS_TO_RESTORE = ['release_date', 'website', 'tags', 'access', 'region', 'name_en']


def get_yaml_from_git(filepath, ref='main'):
    """Get YAML content from a specific git ref."""
    try:
        result = subprocess.run(
            ['git', 'show', f'{ref}:{filepath}'],
            capture_output=True, text=True, check=True
        )
        return yaml.safe_load(result.stdout)
    except (subprocess.CalledProcessError, yaml.YAMLError):
        return None


def get_current_yaml_files():
    """List all current model YAML files."""
    result = subprocess.run(
        ['find', 'domains', '-name', '*.yaml', '!', '-name', '_meta.yaml'],
        capture_output=True, text=True, check=True
    )
    return sorted(result.stdout.strip().split('\n'))


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    yaml_files = get_current_yaml_files()
    total_restored = 0
    files_modified = 0
    
    for filepath in yaml_files:
        # Get the main branch version
        main_data = get_yaml_from_git(filepath, 'main')
        if main_data is None:
            continue
        
        # Read current file
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                current_data = yaml.safe_load(f)
        except (FileNotFoundError, yaml.YAMLError):
            continue
        
        if current_data is None:
            continue
        
        # Check which fields need to be restored
        fields_restored = []
        for field in FIELDS_TO_RESTORE:
            if field not in current_data and field in main_data and main_data[field] is not None:
                current_data[field] = main_data[field]
                fields_restored.append(field)
        
        # Also fix: if current has release_date with 2026, replace with main value
        if 'release_date' in current_data and '2026' in str(current_data.get('release_date', '')):
            if 'release_date' in main_data:
                current_data['release_date'] = main_data['release_date']
                if 'release_date' not in fields_restored:
                    fields_restored.append('release_date')
        
        if fields_restored:
            # Write back the file with restored fields
            # We need to maintain a reasonable field order
            ordered_fields = [
                'name', 'name_en', 'company', 'domain', 'status',
                'release_date', 'website', 'description', 'parameters',
                'architecture', 'base_model', 'training', 'tech_stack',
                'datasets', 'benchmarks', 'api', 'capabilities',
                'tags', 'access', 'region', 'references'
            ]
            
            ordered_data = {}
            for key in ordered_fields:
                if key in current_data:
                    ordered_data[key] = current_data[key]
            # Add any remaining keys not in our order
            for key in current_data:
                if key not in ordered_data:
                    ordered_data[key] = current_data[key]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                yaml.dump(ordered_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)
            
            files_modified += 1
            total_restored += len(fields_restored)
            print(f"  {filepath}: restored {', '.join(fields_restored)}")
    
    print(f"\nSummary: restored {total_restored} fields across {files_modified} files")


if __name__ == '__main__':
    main()
