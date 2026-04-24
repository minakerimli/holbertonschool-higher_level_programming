def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if all items in attendees are dictionaries
    if not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace placeholders
        output = template

        name = attendee.get("name") if attendee.get("name") else "N/A"
        title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(title))
        output = output.replace("{event_date}", str(date))
        output = output.replace("{event_location}", str(location))

        # Write to file
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
