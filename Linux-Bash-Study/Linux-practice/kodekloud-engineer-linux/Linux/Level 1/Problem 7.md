# 🚀 Problem 7: Disable Direct SSH Root Login on All App Servers  

## 📌 Requirement  
Following security audits, the **xFusionCorp Industries** security team has implemented new security protocols, including **restricting direct SSH root login**.  

The task requires **disabling direct SSH root login** on all **app servers** within the **Stratos Datacenter** to enhance security.  

---

## 🔧 Solution  

### **1️⃣ Access Each App Server**  
Use the provided credentials to connect to each **app server** via SSH.  

```bash
ssh tony@stapp01
ssh steve@stapp02
ssh banner@stapp03
