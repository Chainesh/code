from PIL import Image
import os

def remove_chinese_letters(image_path):
    image = Image.open(image_path)
    width, height = image.size
    
    letter_height = 200
    
    upper_region = (0, 0, width, letter_height)
    bottom_region = (0, height - letter_height, width, height)
    modified_image = image.copy()
    
    black_region = Image.new("RGB", (width, letter_height), (0, 0, 0))
    
    modified_image.paste(black_region, (0, 0))
    modified_image.paste(black_region, (0, height - letter_height))
    
    return modified_image


if not os.path.exists("modified_images"):
    os.makedirs("modified_images")

folder_count = 2 

for folder_index in range(1, folder_count + 1):
    folder_path = f"{folder_index}/"  
    modified_folder_path = os.path.join("modified_images", f"{folder_index}") 
    
    # Create a new folder for modified images
    if not os.path.exists(modified_folder_path):
        os.makedirs(modified_folder_path)
    
    for image_name in os.listdir(folder_path):
        if image_name.endswith(".png"):  # Update with your image file extension
            image_path = os.path.join(folder_path, image_name)
            modified_image_path = os.path.join(modified_folder_path, image_name) 
            
            try:
                modified_image = remove_chinese_letters(image_path)
                modified_image.save(modified_image_path)
                
                print(f"Processed image: {modified_image_path}")
            except Exception as e:
                print(f"Error processing image: {image_path}")
                print(str(e))
