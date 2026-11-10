"""
AWS to Azure Workload Assessment CLI
Maps AWS EC2 instance types and EBS storage to optimal Azure VM sizes and Managed Disks.
Author: Vishwjeet Kumar Mehta
"""

import sys

AWS_TO_AZURE_VM_MAP = {
    "t3.medium": "Standard_B2s",
    "t3.large": "Standard_B2ms",
    "m5.large": "Standard_D2s_v5",
    "m5.xlarge": "Standard_D4s_v5",
    "c5.xlarge": "Standard_F4s_v2",
    "r5.xlarge": "Standard_E4s_v5"
}

def map_workload(ec2_type: str, ebs_size_gb: int):
    azure_sku = AWS_TO_AZURE_VM_MAP.get(ec2_type, "Standard_D2s_v5")
    disk_tier = "Premium_LRS" if ebs_size_gb > 128 else "StandardSSD_LRS"
    
    return {
        "source_aws": {"instance_type": ec2_type, "storage_gb": ebs_size_gb},
        "target_azure": {"vm_size": azure_sku, "managed_disk_sku": disk_tier}
    }

if __name__ == "__main__":
    result = map_workload("m5.xlarge", 250)
    print(f"Recommended Azure Sizing: {result}")

