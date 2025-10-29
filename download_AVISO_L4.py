import ftplib
from pathlib import Path

# Update these with your AVISO credentials
AVISO_USERNAME = "USERNAME"
AVISO_PASSWORD = "PASSWORD"
FTP_SERVER = "ftp-access.aviso.altimetry.fr"

# Create a directory to store the data
data_dir = Path("./swot_l4_data")
data_dir.mkdir(exist_ok=True)

print(f"Connecting to {FTP_SERVER}...")
ftp = ftplib.FTP(FTP_SERVER)
ftp.login(user=AVISO_USERNAME, passwd=AVISO_PASSWORD)

path = '/duacs-experimental/dt-phy-grids/l4_karin_nadir/v2.0.1/miost/science'
ftp.cwd(path)

files = []
ftp.retrlines('NLST', files.append)

#This is specifically for the June 2024 data, we will need to update this to download diffetent dates
target_file = None
for f in files:
    if 'dt_global_allsat_phy_l4_20240601' in f and '.nc' in f:
        target_file = f
        print(f"Found: {f}")
        break

if target_file:
    local_file = data_dir / target_file

    if local_file.exists():
        print(f"File exists: {local_file}")
        print(f"Size: {local_file.stat().st_size / (1024**2):.1f} MB")
    else:
        print(f"Downloading {target_file}...")
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f'RETR {target_file}', f.write)

        print(f"Saved: {local_file}")
        print(f"Size: {local_file.stat().st_size / (1024**2):.1f} MB")
else:
    print("File not found")
    print("Files containing '20240601':")
    for f in files:
        if '20240601' in f:
            print(f"  {f}")

ftp.quit()
