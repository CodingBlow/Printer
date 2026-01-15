Python
# Configuration for connecting to ADLS Gen2
storage_account_name = "adlsgen2projectstorage"
container_name = "raw-bronze"
mount_point = "/mnt/bronze"
key = "YOUR_ACCESS_KEY_SECRET" # Retrieved via Key Vault

configs = {
  "fs.azure.account.key." + storage_account_name + ".blob.core.windows.net": key
}

# Check if already mounted, if not, mount it
if not any(mount.mountPoint == mount_point for mount in dbutils.fs.mounts()):
  dbutils.fs.mount(
    source = "wasbs://" + container_name + "@" + storage_account_name + ".blob.core.windows.net",
    mount_point = mount_point,
    extra_configs = configs
  )
  print("Mount Successful!")
else:
  print("Already Mounted.")