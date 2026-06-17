import os
import re
import shutil

# Paths
base_dir = r"d:\DO tech works\new-indian-service-center"
export_dir = os.path.join(base_dir, "php_export")
html_file = os.path.join(base_dir, "core", "templates", "core", "index.html")
php_file = os.path.join(export_dir, "index.php")
static_src = os.path.join(base_dir, "static")
static_dest = os.path.join(export_dir, "static")

# Create export dir
os.makedirs(export_dir, exist_ok=True)

# Copy static files
if os.path.exists(static_dest):
    shutil.rmtree(static_dest)
shutil.copytree(static_src, static_dest)

# Read HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove load static
html = re.sub(r'{%\s*load static\s*%}\n?', '', html)

# Replace static tags
# e.g. {% static 'css/style.css' %} -> static/css/style.css
html = re.sub(r'{%\s*static\s+[\'"]([^\'"]+)[\'"]\s*%}', r'static/\1', html)

# PHP Header
php_code = """<?php
// PHP Backend for New Indian Service Center

// IMPORTANT: Replace these with your Hostinger database details!
$servername = "localhost";
$username = "u123456789_yourdbuser";
$password = "YourNewPassword!";
$dbname = "u123456789_yourdbname";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = isset($_POST['name']) ? $_POST['name'] : 'Not provided';
    $phone = isset($_POST['phone']) ? $_POST['phone'] : 'Not provided';
    $model = isset($_POST['model']) ? $_POST['model'] : 'Not provided';
    $reg = isset($_POST['reg']) ? $_POST['reg'] : '';
    $stype = isset($_POST['stype']) ? $_POST['stype'] : 'Not provided';
    $date_str = isset($_POST['date']) ? $_POST['date'] : '';
    $notes = isset($_POST['notes']) ? $_POST['notes'] : '';

    if (empty($date_str)) {
        $date_val = date('Y-m-d');
    } else {
        $date_val = date('Y-m-d', strtotime($date_str));
    }

    // Connect to database
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check connection (Silently fail so we still redirect to WhatsApp even if DB fails)
    if (!$conn->connect_error) {
        $stmt = $conn->prepare("INSERT INTO bookings (name, phone, vehicle_model, registration_no, service_type, preferred_date, notes) VALUES (?, ?, ?, ?, ?, ?, ?)");
        if ($stmt) {
            $stmt->bind_param("sssssss", $name, $phone, $model, $reg, $stype, $date_val, $notes);
            $stmt->execute();
            $stmt->close();
        }
        $conn->close();
    }

    // Prepare WhatsApp Message
    $message = "*New Service Booking*\\n" .
               "Name: " . $name . "\\n" .
               "Phone: " . $phone . "\\n" .
               "Vehicle: " . $model . "\\n" .
               "Reg No: " . $reg . "\\n" .
               "Service: " . $stype . "\\n" .
               "Date: " . $date_val . "\\n" .
               "Notes: " . $notes;

    $encoded_message = urlencode($message);
    $target_number = "918075856132"; // The target WhatsApp number

    $whatsapp_url = "https://wa.me/" . $target_number . "?text=" . $encoded_message;

    // Redirect to WhatsApp
    header("Location: " . $whatsapp_url);
    exit();
}
?>
"""

# Write PHP file
with open(php_file, 'w', encoding='utf-8') as f:
    f.write(php_code + html)

print("PHP file generated successfully!")

# Generate SQL file
sql_code = """
CREATE TABLE `bookings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `vehicle_model` varchar(100) NOT NULL,
  `registration_no` varchar(50) NOT NULL,
  `service_type` varchar(100) NOT NULL,
  `preferred_date` date NOT NULL,
  `notes` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

sql_file = os.path.join(export_dir, "database.sql")
with open(sql_file, 'w', encoding='utf-8') as f:
    f.write(sql_code)
print("SQL file generated successfully!")
