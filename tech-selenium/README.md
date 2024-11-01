# 使用 python selenium

## 資訊

用 URL 做測試
`data.py`去比較選出答案

### 如何使用selenium
```
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
```

## 執行

### 安裝python庫
```bash
pip install -r requirements.txt
```

### 設定資訊
```bash
cp .env.example .env
```

### 執行
```bash
python main.py
```
