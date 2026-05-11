import yt_dlp
import os

def show_formats(url):
    ydl_opts = {"quiet": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    print(f"\nВидео: {info['title']}")
    print(f"Длительность: {info['duration'] // 60} мин {info['duration'] % 60} сек\n")

    formats = []
    seen = set()

    for f in info["formats"]:
        height = f.get("height")
        ext = f.get("ext")
        vcodec = f.get("vcodec", "none")
        acodec = f.get("acodec", "none")
        filesize = f.get("filesize") or f.get("filesize_approx")

        if height and vcodec != "none" and acodec != "none" and ext == "mp4":
            key = (height, ext)
            if key not in seen:
                seen.add(key)
                size_str = f"{filesize / 1024 / 1024:.1f} МБ" if filesize else "неизвестно"
                formats.append((height, ext, size_str, f["format_id"]))

    if not formats:
        for f in info["formats"]:
            height = f.get("height")
            ext = f.get("ext")
            vcodec = f.get("vcodec", "none")
            filesize = f.get("filesize") or f.get("filesize_approx")
            if height and vcodec != "none":
                key = (height, ext)
                if key not in seen:
                    seen.add(key)
                    size_str = f"{filesize / 1024 / 1024:.1f} МБ" if filesize else "неизвестно"
                    formats.append((height, ext, size_str, f["format_id"]))

    formats.sort(key=lambda x: x[0], reverse=True)

    print("Доступные качества:")
    print(f"{'№':<4} {'Качество':<12} {'Формат':<8} {'Размер'}")
    print("-" * 36)
    for i, (height, ext, size, _) in enumerate(formats):
        print(f"{i+1:<4} {str(height) + 'p':<12} {ext:<8} {size}")

    return formats, info["title"]


def download_video(url, format_id, title):
    output_dir = os.path.expanduser("~/Downloads")
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        "format": f"{format_id}+bestaudio/best[height<={format_id}]",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "progress_hooks": [progress_hook],
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"\nГотово! Файл сохранён в: {output_dir}")


def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "?%").strip()
        speed = d.get("_speed_str", "?").strip()
        eta = d.get("_eta_str", "?").strip()
        print(f"\r  Загрузка: {percent}  Скорость: {speed}  Осталось: {eta}   ", end="")
    elif d["status"] == "finished":
        print(f"\r  Загрузка завершена. Обработка...                          ")


def main():
    print("=== Загрузчик видео с YouTube ===\n")
    url = input("Вставьте ссылку на видео: ").strip()

    if not url:
        print("Ссылка не указана.")
        return

    print("\nПолучаю информацию о видео...")

    try:
        formats, title = show_formats(url)
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    if not formats:
        print("Не удалось получить список форматов.")
        return

    print()
    while True:
        choice = input(f"Выберите номер качества (1–{len(formats)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(formats):
            break
        print("Неверный выбор, попробуйте ещё раз.")

    selected = formats[int(choice) - 1]
    height, ext, size, format_id = selected
    print(f"\nВыбрано: {height}p  ({size})")
    print("Начинаю загрузку...\n")

    try:
        download_video(url, format_id, title)
    except Exception as e:
        print(f"\nОшибка при загрузке: {e}")


if __name__ == "__main__":
    main()