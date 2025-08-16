#!/bin/bash
# Настройка локального Git для daily-python-education

cd ~/Desktop/daily-python-education

# Инициализация, если не сделано
if [ ! -d ".git" ]; then
    git init
    git branch -M main
fi

# Настройка локального email и имени
git config --local user.email "alekincoding@gmail.com"
git config --local user.name "AlekinCoding"

# Настройка remote
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/AlekinCoding/daily-python.git

# Создание начального README, если репозиторий пустой
if [ ! -f "README.md" ]; then
    echo "# Daily Python" > README.md
    echo "Репозиторий для ежедневных упражнений и заметок по Python" >> README.md
    git add README.md
    git commit -m "Initial commit"
    git push -u origin main
fi

echo "Готово! Репозиторий настроен для alekincoding@gmail.com"