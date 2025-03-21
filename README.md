# RVU-Wifi-Captive-Portal-Resolver 🔒🤖  
A Python-based tool designed to help students and professors at RV University automatically log into captive portals, streamlining Wi-Fi access. 🌐🎓

## Why I Created This Project 🤔  
As someone who values **online privacy** and security, I  use **Private DNS** services like AdGuard or Cloudflare. However, these services can sometimes interfere with captive portals, such as the one at RV University. The login process requires multiple steps:

1. Disable Private DNS,  
2. Access the captive portal and log in,  
3. Re-enable Private DNS.

I realized that many students and professors, especially on devices like MacBooks and laptops using Google Chrome's Secure DNS, face a similar issue where the captive portal doesn't automatically pop up. This inspired me to create a tool that automates the login process, saving time and hassle for everyone. 🚀

## Features ✨  
- 🔑 **Automated login** to captive portals  
- ⚙️ **Customizable credentials** and URL  
- 🕵️‍♂️ **Browser-like headers** for stealthy interaction  
- ✅ **Error handling** with success verification  
- 🖥️ **Command-line interface (CLI)** with argument support  

## Prerequisites 🛠️  
- Python 3.6+  
- `requests` library (for HTTP requests)  
- `argparse` (for handling command-line arguments)  
- `time` and `urllib.parse` (standard Python libraries, no installation required)  

## Installation 📥  
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/captive-portal-automator.git
   cd captive-portal-automator
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

### Dependencies Breakdown:
- **`requests`**: For sending HTTP requests to the captive portal.  
- **`argparse`**: For handling command-line arguments.  
- **`time`**: Part of the standard Python library, used for adding timestamps in the payload.  
- **`urllib.parse`**: Part of the standard Python library, used for parsing URLs.  

## Usage 🎬  
Run the script with the following command:
```bash
python captive_portal_login.py [-h] [-u USERNAME] [-p PASSWORD] [-l LOGIN_URL]
```

### Command-Line Arguments 🔧
| Argument | Default Value | Description |
|----------|---------------|-------------|
| `-u` | Test | Your portal username |
| `-p` | Test | Your portal password |
| `-l` | https://172.16.0.1:8090/login.xml | Portal login URL |

### Example 💡  
```bash
python captive_portal_login.py -u myuser -p mypass -l https://newportal/login.xml
```

## How It Works 🛠️  
1. The script sends a **POST request** with browser-like headers to the captive portal.  
2. It includes a **timestamp** in the payload for authentication.  
3. It **verifies** the response for success indicators.  
4. It handles **network errors gracefully**, providing feedback on the login attempt.  

### Error Handling:  
- If the **username** or **password** is incorrect, the program will return a **200 OK** status code, but the response will contain the following message:  
  ```
  Status Code: 200  
  Response Body: <?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[Login failed. Invalid user name/password. Please contact the administrator. ]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state><user><![CDATA[]]></user></requestresponse>
  ```
  This indicates that the login attempt was unsuccessful, even though the status code is `200`. This happens because captive portals often return a successful status even when login fails.  

- If the **URL** is incorrect, you will receive an error message like:  
  ```
  Request failed: 404 Client Error: File not found for url: https://example.com
  ```  
  This indicates that the URL you provided could not be found on the server.  

### Verifying Successful Login:  
Due to the way captive portals handle login responses, the program cannot directly confirm if the login was successful. To verify, you will need to **manually check**:  
1. **Open Google Chrome** and see if the captive portal page automatically loads.  
2. Alternatively, try opening any website—if the page loads without redirection to the captive portal, it means the login was successful.

If the portal does appear or you are redirected to it, the login attempt was likely unsuccessful.

## Demo 🎥

### Normal way

![Before Video](https://github.com/KumarSrinidhi/RVU-Wifi-Captive-Portal-Resolver/blob/main/videos/Before.gif?raw=true)

### With the help of captive_portal_login.py

![After Video](https://github.com/KumarSrinidhi/RVU-Wifi-Captive-Portal-Resolver/blob/main/videos/after.gif?raw=true)

## Security Note ⚠️  
⚠️ The script uses `verify=False` for self-signed certificates. **For production use**:  
- Specify a CA bundle path.  
- Never hardcode your credentials in the script for security reasons.

## Disclaimer ⚠️  
This project was created **out of curiosity** and is a **basic version**. It may contain bugs or be incomplete. I am **not responsible for any loss, harm, or damage** caused by the use of this software. Use at your own risk and test it thoroughly before depending on it.

## Contributing 🤝  
Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## License 📜  
This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

---

Made with ❤️ by Kumar Srinidhi
