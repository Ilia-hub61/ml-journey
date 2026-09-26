def add_setting(settings, keys):
    key, value = keys
    key = key.lower()
    value = value.lower()
    if key in settings:
        return (f"Setting '{key}' already exists! Cannot add a new setting"
                f" with this name.")
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, keys):
    key, value = keys
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing"
                f" setting.")


def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings):
    if not settings:
        return 'No settings available.'
    else:
        s = "Current User Settings:"
        for item, key in settings.items():
            s += f'\n{item.title()}: {key}'
        return s + '\n'


test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled'
}

print(add_setting(test_settings, ('Volume', 'High')))
print(test_settings)

print(add_setting(test_settings, ('Theme', 'Light')))
print(test_settings)

print(update_setting(test_settings, ('Theme', 'Light')))
print(test_settings)

print(update_setting(test_settings, ('Font', 'Arial')))
print(test_settings)

print(delete_setting(test_settings, 'Language'))
print(test_settings)

print(delete_setting(test_settings, 'Font'))
print(test_settings)

print(view_settings(test_settings))
print(view_settings({}))
