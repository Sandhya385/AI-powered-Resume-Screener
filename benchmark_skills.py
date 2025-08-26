# ✅ Benchmark skills (normalized, lowercase where applicable)
benchmark_skills = [
    '2g', '3g', '4g', '5g', 'adobe photoshop', 'android studio', 'arduino',
    'assembly language', 'banking', 'bidding', 'bidding expert', 'bidding strategies',
    'budgeting', 'business analysis', 'business development', 'business development & management',
    'business relationship management', 'business strategy', 'capital budgeting', 'circuit analysis',
    'circuit designing', 'client relationship management', 'computer sciences', 'content marketing',
    'cross functional development', 'customer service', 'data extraction', 'digital marketing',
    'digital media strategy', 'ecommerce management', 'electrical design evaluation',
    'electrical wiring', 'electronic circuits', 'email campaigns', 'email marketing',
    'enterprise sales', 'financial management', 'freelancer', 'freshdesk', 'functional safety',
    'google analytics', 'graphic designing', 'installation', 'inventory control', 'key account management',
    'lead generation', 'management', 'market analysis', 'market development', 'microsoft office',
    'microsoft outlook', 'motor winding', 'operations management', 'pain points/requirement analysis',
    'payroll', 'portfolio management', 'power system analysis', 'process improvement', 'procurement',
    'project costing and budgeting', 'project management', 'proposal development', 'proposal writing',
    'relevant software and technologies', 'repairing of appliances', 'rockwell controllogix',
    'sales & customer services', 'sales execution', 'sales forecasting', 'sales management', 'sales navigator',
    'sales pipeline management', 'salesforce', 'scratch', 'sensor interfacing', 'serenade', 'shopify',
    'social media marketing', 'staff hiring & training', 'tableau', 'team leadership', 'team management',
    'testing & commissioning', 'typing speed 40wpm', 'vendor management', 'vendor relationship management',
    'web & mobile development', 'web content development', 'welding', 'wireless integration',
    'wonderware intouch', 'zendesk', 'aeroleads', 'agile', 'asana', 'autocad', 'b2b lead generation',
    'bizz trax', 'c', 'c#', 'c++', 'canva', 'cisco packet tracer', 'click up', 'cloud cme',
    'conducting fat / sat', 'crm implementation', 'css', 'data analysis', 'direct sales', 'enodeb',
    'esp controllers', 'excel', 'facebook ads', 'fiverr', 'gnodeb integration', 'google adwords',
    'google suite', 'gsm', 'helioscope', 'html', 'huawei oss 2020', 'hubspot', 'ibm spss', 'igms',
    'java', 'jira', 'krayin crm', 'labview', 'ladder logic', 'linkedin', 'lte', 'matlab',
    'microsoft office', 'microsoft project', 'mml', 'multisim', 'multism', 'mw management',
    'netbeans', 'nodeb', 'odoo', 'osisoft pi', 'oss mae', 'pcb designing', 'power bi', 'powerpoint',
    'pph', 'proteus', 'python', 'quickbooks', 'radio access network (ran)', 'sales', 'sdlc',
    'seo', 'siemens tia portal', 'simulink', 'slack', 'sm', 'smart pls', 'spss', 'sql', 'sran scripting',
    'stata', 'tcp/ip', 'trello', 'umts', 'unity', 'upwork', 'vba', 'vegas pro', 'vhdl', 'visual studio',
    'voip', 'web cme', 'word', 'wordpress', 'zoho', 'XGBoost','LightGBM','hypothesis testing','probability',
    'scikitlearn','machine learning','classification','regression',' logistic regression','decision trees',
    'random forests','SVMs','boosting','exploratory data analysis','EDA', 'statistical','Data Science'
]

# Skill normalization dictionary (expanded)
skill_map = {
    "ms excel": "excel",
    "microsoft excel": "excel",
    "excel": "excel",
    "ms word": "word",
    "microsoft word": "word",
    "ms powerpoint": "powerpoint",
    "microsoft powerpoint": "powerpoint",
    "ms projects": "microsoft project",
    "microsoft project": "microsoft project",
    "g suite": "google suite",
    "g-suite": "google suite",
    "google analytics 360": "google analytics",
    "power bi desktop": "power bi",
    "tableau desktop": "tableau",
    "adobe ps": "adobe photoshop",
    "photoshop": "adobe photoshop",
    "c plus plus": "c++",
    "c sharp": "c#",
    "microsoft outlook": "outlook",
    "ms outlook": "outlook",
    "ms visio": "visio",
    "microsoft visio": "visio",
    "linkedin sales navigator": "sales navigator",
    "fb ads": "facebook ads",
    "facebook advertising": "facebook ads",
    "google adwords": "google ads",
    "gads": "google ads",
    "crm": "crm implementation",
    "hubspot crm": "hubspot",
    "salesforce crm": "salesforce",
    "project management professional": "project management",
    "pmp": "project management",
    "sap": "sap erp",
    "erp": "erp system",
    "powerpoint presentation": "powerpoint",
    "word processing": "word",
    "excel spreadsheet": "excel",
    "photoshop cc": "adobe photoshop",
    "adobe illustrator": "illustrator",
    "ai": "illustrator",
    "email marketing campaign": "email marketing",
    "social media marketing campaign": "social media marketing",
}

def normalize_skill(skill):
    skill=skill.lower().strip()
    return skill_map.get(skill,skill)

def extract_skill(text):
    text=text.lower()
    found=[]
    for skill in benchmark_skills:
        if skill.lower() in text:
            found.append(normalize_skill(skill))
    return set(found)

def find_gaps(resume_text,job_description):
    #Identify missing key skills/keywords
    resume_skills=extract_skill(resume_text)
    jd_skills=extract_skill(job_description)

    matched=resume_skills & jd_skills
    missing=jd_skills-resume_skills
    extra=resume_skills-jd_skills

    return matched, missing, extra