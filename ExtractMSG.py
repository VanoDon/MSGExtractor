import os
import extract_msg

def extract_attachments(msg_file, output_folder):
    try:
        msg = extract_msg.Message(msg_file)
        msg_subject = msg.subject
        for attachment in msg.attachments:
            attachment_filename = attachment.longFilename or attachment.shortFilename or 'unknown'
            attachment_path = os.path.join(output_folder, attachment_filename)
            with open(attachment_path, 'wb') as f:
                f.write(attachment.data)
            print(f"Extracted '{attachment_filename}' from '{msg_subject}'")
    except Exception as e:
        print(f"Failed to process {msg_file}: {e}")

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.msg'):
                msg_file_path = os.path.join(root, file)
                extract_attachments(msg_file_path, output_folder)

if __name__ == "__main__":
    input_folder = 'input'  # Replace with the path to your input folder
    output_folder = 'Done'  # Replace with the path to your output folder
    main(input_folder, output_folder)
