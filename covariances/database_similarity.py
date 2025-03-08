def jaccard_index(list1, list2):
    set1, set2 = set(list1), set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union) if len(union) != 0 else 0

# Example lists
list1_trivy = ["secdb", "Amazon Linux Security Center", "Security Bug Tracker", "Ubuntu CVE Tracker", "OVAL",
"CVRF", "Photon Security Advisory", "PHP Security Advisories Database", "GitHub Security Advisories", "Safety DB",
"Ruby Advisory Database", "Ecosystem Security Working Group", "GitLab Advisories Community", "Golang VulnDB",
"RustSec Advisory Database", "NVD"]
list2_grype = ["Alpine Linux SecDB", "Amazon Linux ALAS", "Chainguard SecDB", "Debian Linux CVE Tracker",
"GitHub Security Advisories", "NVD", "OVAL", "RedHat Security Data", "RedHat RHSAs", "SUSE Linux OVAL",
"Ubuntu Linux Security", "Wolfi SecDB"]
list3_depscan = ["OSV", "NVD", "GitHub Security Advisories", "NPM", "Linux vuln-list"]
list4_osv = ["GitHub Security Advisories", "PyPI Advisory Database", "Golang VulnDB", "RustSec Advisory Database",
"Global Security Database", "OSS-Fuzz", "Rocky Linux", "AlmaLinux", "Haskell Security Advisories",
"RConsortium Advisory Database", "OpenSSF Malicious Packages", "Python Software Foundation Database", 
"Bitnami Vulnerability Database", "Haskell Security Advisory DB", "Ubuntu CVE Tracker"]
list5_vexy = ["OSV", "OSS Index"]
list6_scout = ["Alpine secdb", "AlmaLinux", "Amazon Linux Security Center", "Bitnami Vulnerability Database",
"CISA Known Exploited Vulnerability Catalog", "CISA Vulnrichment", "Security Bug Tracker", "Exploit Prediction Scoring System",
"GitHub Security Advisories", "GitLab Advisories Community", "Golang VulnDB", "NVD", "Oracle Linux Security",
"PyPI Advisory Database", "RedHat Security Data", "Rocky Linux", "RustSec Advisory Database", "SUSE Linux OVAL",
"Ubuntu CVE Tracker", "Wolfi SecDB", "Chainguard Security Feed"]
list7_snyk = ["NVD", "OSS Index", "NPM", "Ruby Advisory Database", "Python Software Foundation Database",
"GitHub Security Advisories", "RustSec Advisory Database", "Golang VulnDB", "Snyk Vulnerability Database"]

# Calculate Jaccard Index
jaccard_score = jaccard_index(list4_osv, list5_vexy)
print(f"Jaccard Index: {jaccard_score}")