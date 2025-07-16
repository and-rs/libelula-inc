import subprocess


if __name__ == "__main__":
    _ = subprocess.run(
        [
            "tailwindcss",
            "-i",
            "app/static/input.css",
            "-o",
            "app/static/output.css",
            "--watch",
        ]
    )
