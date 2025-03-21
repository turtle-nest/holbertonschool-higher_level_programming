def generate_invitations(template, attendees):
    """Generates personalized invitation files from a template and a list of attendees."""
    if not isinstance(template, str):
        print("Error: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees):
        text = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = str(attendee.get(key) or "N/A")
            text = text.replace(f'{{{key}}}', value)
        filename = f'output_{index + 1}.txt'
        try:
            with open(filename, 'w') as f:
                f.write(text)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
