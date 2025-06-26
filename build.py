import platform
import os

def main():
    system = platform.system().lower()
    machine = platform.machine().lower()

    keep_keywords = []
    if system == "windows":
        keep_keywords = ["windows"]
        if "64" in machine:
            keep_keywords.append("64")
        else:
            keep_keywords.append("32")
    elif system == "linux":
        keep_keywords = ["linux"]
        if "arm" in machine:
            keep_keywords.append("arm")
        elif "aarch64" in machine:
            keep_keywords.append("arm64")
        elif "x86_64" in machine or "amd64" in machine:
            keep_keywords.append("amd64")
    elif system == "darwin":
        keep_keywords = ["darwin"]
        if "arm" in machine:
            keep_keywords.append("arm64")
        else:
            keep_keywords.append("amd64")

    libs_dir = os.path.join(os.path.dirname(__file__), "src", "htls", "libs")
    for filename in os.listdir(libs_dir):
        if not all(k in filename for k in keep_keywords):
            os.remove(os.path.join(libs_dir, filename))
            print(f"Removed: {filename}")

if __name__ == "__main__":
    main()
