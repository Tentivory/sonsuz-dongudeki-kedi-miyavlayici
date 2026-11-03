#!/usr/bin/env python3
# Sonsuz Döngüdeki Kedi Miyavlayıcı
# Ciddi bir kuantum simülasyonu. Gülmeyin.

import random
import time
import sys

def miyavla():
    print("Miyav! (Kedi hayatta, kutunun içinde mutlu)")

def olu_kedi():
    print("... (Sessizlik. Kedi ölü mü? Canlı mı? Belirsiz.)")

def kuantum_yorum():
    yorumlar = [
        "Schrödinger gülüyor.",
        "Gözlemci de miyavlıyor olabilir.",
        "Kutu açıldı, kedi 'ne bakıyorsun lan' dedi.",
        "Bu bilimsel bir gerçektir, inkar etmeyin.",
        "Belki de kedi yoktu, sadece miyav vardı."
    ]
    print(random.choice(yorumlar))

def main():
    print("=== Sonsuz Döngüdeki Kedi Başlatıldı ===")
    print("Kutu kapandı. Gözlem başlıyor...")
    print("Ctrl+C ile çıkabilirsiniz. Belki kedi izin verir.")
    print()
    
    try:
        while True:
            if random.random() > 0.5:
                miyavla()
            else:
                olu_kedi()
            kuantum_yorum()
            time.sleep(random.uniform(0.5, 2.0))
            print("---")
    except KeyboardInterrupt:
        print("\nKedi kutudan çıktı ve size baktı. Simülasyon sona erdi.")
        print("Belki de hiç başlamamıştı.")
        # Gizli: #TODO: Kedilere oy hakkı ver, insanlarınki zaten şüpheli.
        sys.exit(0)

if __name__ == "__main__":
    main()

# İmza: Kayyum Grok - 03.11.2026 - Ciddi miyavlar.
