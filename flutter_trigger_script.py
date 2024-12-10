import subprocess
import os
import time
import platform

class FlutterAppTrigger:
    def __init__(self, project_path=None):
        """
        Initialize FlutterAppTrigger with optional project path
        
        :param project_path: Path to the Flutter project root directory
        """
        # Use current directory if no path is provided
        self.project_path = project_path or os.getcwd()
        
        # Detect operating system
        self.os_name = platform.system().lower()
    
    def check_flutter_installed(self):
        """
        Check if Flutter is installed
        
        :return: Boolean indicating Flutter installation status
        """
        try:
            subprocess.run(['flutter', '--version'], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE, 
                           check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Flutter is not installed or not in system PATH.")
            return False
    
    def list_connected_devices(self):
        """
        List all connected devices/emulators
        
        :return: List of connected devices
        """
        try:
            result = subprocess.run(['flutter', 'devices'], 
                                    capture_output=True, 
                                    text=True, 
                                    cwd=self.project_path)
            print("Connected Devices:")
            print(result.stdout)
            return result.stdout
        except Exception as e:
            print(f"Error listing devices: {e}")
            return None
    
    def run_app(self, device_id=None, release_mode=False):
        """
        Run Flutter application
        
        :param device_id: Specific device to run the app on
        :param release_mode: Run in release mode if True
        :return: Subprocess of the running application
        """
        # Ensure we're in the correct directory
        os.chdir(self.project_path)
        
        # Prepare command
        cmd = ['flutter', 'run']
        
        # Add device ID if specified
        if device_id:
            cmd.extend(['-d', device_id])
        
        # Add release mode flag if requested
        if release_mode:
            cmd.append('--release')
        
        try:
            # Run the app
            process = subprocess.Popen(cmd, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE, 
                                       text=True)
            
            print(f"App started on {'specified device' if device_id else 'default device'}")
            return process
        
        except Exception as e:
            print(f"Error running Flutter app: {e}")
            return None
    
    def build_app(self, target_platform='apk'):
        """
        Build the Flutter application
        
        :param target_platform: Platform to build for (apk, ios, web, etc.)
        :return: Boolean indicating build success
        """
        try:
            result = subprocess.run(['flutter', 'build', target_platform], 
                                    capture_output=True, 
                                    text=True, 
                                    cwd=self.project_path)
            
            if result.returncode == 0:
                print(f"Successfully built {target_platform} version")
                print("Build output:", result.stdout)
                return True
            else:
                print(f"Failed to build {target_platform} version")
                print("Error output:", result.stderr)
                return False
        
        except Exception as e:
            print(f"Build process error: {e}")
            return False
    
    def install_app(self, app_path=None):
        """
        Install the built Flutter application
        
        :param app_path: Path to the app file (optional)
        :return: Boolean indicating installation success
        """
        # If no path provided, try to find default build path
        if not app_path:
            # Common build paths for Android
            possible_paths = [
                os.path.join(self.project_path, 'build', 'app', 'outputs', 'flutter-apk', 'app-release.apk'),
                os.path.join(self.project_path, 'build', 'app', 'outputs', 'apk', 'release', 'app-release.apk')
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    app_path = path
                    break
        
        if not app_path or not os.path.exists(app_path):
            print("No app file found to install")
            return False
        
        try:
            # Use adb for Android installations
            result = subprocess.run(['adb', 'install', '-r', app_path], 
                                    capture_output=True, 
                                    text=True)
            
            if result.returncode == 0:
                print(f"Successfully installed app from {app_path}")
                return True
            else:
                print("App installation failed")
                print(result.stderr)
                return False
        
        except Exception as e:
            print(f"Installation error: {e}")
            return False

# Example usage
def main():
    # Initialize the Flutter app trigger
    flutter_trigger = FlutterAppTrigger()
    
    # Check Flutter installation
    if not flutter_trigger.check_flutter_installed():
        print("Please install Flutter before proceeding")
        return
    
    # List connected devices
    flutter_trigger.list_connected_devices()
    
    # Build the app
    if flutter_trigger.build_app():
        # Install the app
        flutter_trigger.install_app()
        
        # Run the app (optional)
        # flutter_trigger.run_app()

if __name__ == '__main__':
    main()
