<div align="center">

# ☁️ AWS to Azure Enterprise Workload Migrator

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?style=for-the-badge&logo=ansible&logoColor=white)](https://www.ansible.com/)
[![Terraform](https://img.shields.io/badge/Terraform-Target_Infra-844FBA?style=for-the-badge&logo=terraform&logoColor=white)](https://www.terraform.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](./LICENSE)

<p align="center">
  <b>Comprehensive enterprise cross-cloud migration automation suite providing automated AWS EC2 discovery, Azure VM SKU recommendation engine, and Ansible cutover playbooks with WALinuxAgent injection.</b>
</p>

</div>

---

## 🚀 Migration Lifecycle

```
[ AWS Environment ]                         [ Azure Environment ]
  - EC2 Instance Inventory                    - Terraform Target VNet
  - EBS Storage Metrics                       - Azure Managed Disks
           │                                            ▲
           ▼                                            │
┌─────────────────────────┐                             │
│ Python Assessment CLI   │ ──(Optimal SKU Mapping)─────┤
└──────────┬──────────────┘                             │
           │                                            │
           ▼                                            │
┌─────────────────────────┐                             │
│ Ansible Cutover Playbook│ ──(Driver/Agent Injection)──┘
└─────────────────────────┘
```

---

## 📁 Repository Layout

```
aws-to-azure-workload-migrator/
├── .github/workflows/
│   └── ci.yml                     # Automated regression validation
├── src/
│   └── assessment_cli.py          # AWS EC2 to Azure VM mapping algorithm
├── ansible/playbooks/
│   └── migrate-vm.yml             # System preparation & WALinuxAgent installation
├── terraform/
│   └── azure-target-env.tf        # Target subscription landing network
└── README.md
```

---

## 👤 Author

**Vishwjeet Kumar Mehta**  
Senior DevOps & DevSecOps Consultant | Cloud & Infrastructure Architect  
- **LinkedIn**: [linkedin.com/in/vishwjeetmehta](https://linkedin.com/in/vishwjeetmehta)  
- **GitHub**: [@vishwjeetmehta-bot](https://github.com/vishwjeetmehta-bot)
