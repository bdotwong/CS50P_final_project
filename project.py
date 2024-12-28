import os
import time
import argparse
import tkinter as tk
from PIL import Image, ImageTk
from picamera2 import Picamera2

def main():
    args = parse_args()

    capture_images(
        output_dir="images",
        num_images=args.images,
        interval=args.time,
        display=args.display,
    )

    print(f"Captured {args.images} images. Images are saved in the 'images' folder.")

    # Create GIF
    image_files = [
        os.path.join("images", f"image_{i+1}.jpg") for i in range(args.images)
    ]
    images = [Image.open(img) for img in image_files]
    create_gif(images, "output.gif", args.size)
    print("GIF created: output.gif")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Capture images and create a stop-motion GIF."
    )
    parser.add_argument(
        "--images",
        type=int,
        default=10,
        help="Number of images to capture (default: 10).",
    )
    parser.add_argument(
        "--time",
        type=float,
        default=2,
        help="Time interval (in seconds) between captures (default: 2).",
    )
    parser.add_argument(
        "--display",
        type=bool,
        default=True,
        help="Whether to display images in a Tkinter window during capture (default: True).",
    )
    parser.add_argument(
        "--size",
        type=str,
        default="medium",
        choices=["small", "medium", "xl"],
        help="Size of the GIF: small, medium, or xl (default: medium).",
    )
    return parser.parse_args()


def capture_images(output_dir, num_images, interval, display):
    """Capture images using the Raspberry Pi camera and optionally display them."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    camera = Picamera2()
    camera.start()

    if display:
        window = tk.Tk()
        window.title("Capturing Images")
        label = tk.Label(window)
        label.pack()

    for i in range(num_images):
        img_path = os.path.join(output_dir, f"image_{i+1}.jpg")
        camera.capture_file(img_path)
        print(f"Captured {img_path}")

        if display:
            img = Image.open(img_path)
            img = img.resize((400, 300))
            tk_img = ImageTk.PhotoImage(img)
            label.config(image=tk_img)
            label.image = tk_img
            window.update()

        time.sleep(interval)

    # Cleanup
    camera.close()
    if display:
        window.destroy()


def create_gif(images, output_path, size):
    resolution = gif_resolution(size)
    resized_images = [img.resize(resolution, Image.ANTIALIAS) for img in images]
    resized_images[0].save(
        output_path,
        save_all=True,
        append_images=resized_images[1:],
        duration=500,  # Duration per frame in milliseconds
        loop=0  # Infinite loop
    )


def gif_resolution(size):
    resolutions = {
        "small": (320, 240),  
        "medium": (640, 480), 
        "xl": (1280, 960) 
    }
    return resolutions[size]


if __name__ == "__main__":
    main()
