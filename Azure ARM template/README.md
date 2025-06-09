#  Azure Virtual Machine Deployment Template

This repository contains an [Azure Resource Manager (ARM)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) template to deploy a **Virtual Machine** along with a **Virtual Network (VNet)**, **Subnet**, and **Network Interface (NIC)** in Microsoft Azure.

---

##  Resources Deployed

This ARM template deploys the following Azure resources:

- **Virtual Network (VNet)** with a specified address space
- **Subnet** inside the VNet
- **Network Interface (NIC)** connected to the subnet
- **Virtual Machine (VM)** with customizable size and credentials

---

##  Parameters

| Parameter       | Type         | Description                                   | Example / Default      |
|----------------|--------------|-----------------------------------------------|-------------------------|
| `location`      | `string`     | Azure region to deploy resources              | `"East US"`             |
| `vmSize`        | `string`     | Size of the VM                                | `"Standard_B1s"`        |
| `adminUsername` | `string`     | Admin username for the VM                     | `"azureadmin"`          |
| `adminPassword` | `secureString` | Admin password (secured)                    | Prompted at deployment  |
| `vnetName`      | `string`     | Name of the virtual network                   | `"myVNet"`              |
| `subnetName`    | `string`     | Name of the subnet within the VNet            | `"mySubnet"`            |

---

##  Template Files

- `azuredeploy.json` – Main ARM template
- (Optional) `azuredeploy.parameters.json` – Parameters file (not included by default)

---

##  Deployment Instructions

### Option 1: Azure Portal

1. Go to the [Azure Portal](https://portal.azure.com/)
2. Search for **"Deploy a custom template"**
3. Upload the `azuredeploy.json` file
4. Fill in the required parameters
5. Click **Review + Create**

### Option 2: Azure CLI

```bash
az deployment group create \
  --resource-group <your-resource-group> \
  --template-file azuredeploy.json \
  --parameters adminUsername=<your-username> adminPassword=<your-password>
  ```

## Security Notes
- Avoid hardcoding passwords. Always use the secureString parameter and pass secrets securely at runtime.

- Consider integrating with Azure Key Vault for secret management in production.