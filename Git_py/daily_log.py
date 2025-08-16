import subprocess
from datetime import date
from pathlib import Path

# === Настройка ===
REPO_PATH = Path(r"C:\Users\alexu\Desktop\daily-python-education")
LOG_DIR = REPO_PATH / "daily_plan"

def main():
    today = date.today().isoformat()
    log_file = LOG_DIR / f"{today}.md"

    # Задаём вопросы
    done_today = input("Что сделано за сегодня: ").strip()
    learned = input("Что изучено: ").strip()
    plans = input("Какие планы: ").strip()

    # Создаём папку, если нет
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Записываем в файл Markdown
    content = f"""# {today}

Что сделано за сегодня: {done_today}

Что изучено: {learned}

Какие планы: {plans}
"""
    log_file.write_text(content, encoding="utf-8")
    print(f"Создан лог: {log_file}")

    # git add
    relative_path = f"daily_plan/{today}.md"
    subprocess.run(["git", "-C", str(REPO_PATH), "add", relative_path], check=True)

    # git commit
    commit_msg = f"{today}: daily log"
    result = subprocess.run(
        ["git", "-C", str(REPO_PATH), "commit", "-m", commit_msg],
        capture_output=True, text=True
    )

    if "nothing to commit" in result.stdout.lower() or "nothing to commit" in result.stderr.lower():
        print("Нет изменений — коммит не создан.")
    else:
        # git push
        push_result = subprocess.run(["git", "-C", str(REPO_PATH), "push", "origin", "main"], capture_output=True, text=True)
        if push_result.returncode == 0:
            print(f"✅ Лог за {today} отправлен в GitHub.")
        else:
            print(f"❌ Ошибка при push: {push_result.stderr}")

if __name__ == "__main__":
    main()