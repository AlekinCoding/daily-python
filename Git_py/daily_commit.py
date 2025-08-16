import sys
import subprocess
from datetime import date
from pathlib import Path

# === Настройка ===
REPO_PATH = Path(r"C:\Users\alexu\Desktop\daily-python-education")

def main():
    today = date.today().isoformat()

    if len(sys.argv) == 2:
        relative_path = sys.argv[1]
    else:
        # Интерактивный режим: спрашиваем путь
        relative_path = input("Куда сохранить в гит (например, weather.py или project/aivoice.py): ").strip()

    if not relative_path:
        print("Путь не указан — выход.")
        return

    target = REPO_PATH / relative_path

    if not target.exists():
        # Создаём папки и пустой файл, если нужно
        target.parent.mkdir(parents=True, exist_ok=True)
        target.touch()
        print(f"Создан новый файл: {relative_path}")

    # git add
    subprocess.run(["git", "-C", str(REPO_PATH), "add", relative_path], check=True)

    # git commit
    commit_msg = f"{today}: add/update {relative_path}"
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
            print(f"✅ Файл {relative_path} сохранён в GitHub: {commit_msg}")
        else:
            print(f"❌ Ошибка при push: {push_result.stderr}")

if __name__ == "__main__":
    main()