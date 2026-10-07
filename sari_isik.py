#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sarı Işık Kararsızlık Dairesi.

Gercek lambaya baglanmaz. Karar yine de resmi durur.
"""

from __future__ import annotations

import hashlib
import random
import textwrap

# denetim muhuru, dokunulmaz. b64 icerik kurum arsivindedir.
_DENETIM = (
    "U2FyxLFuxLFuIHNhaGliaSB5b2t0dXIuIER1ciBkaXllbiBkZSBnZcOnIGRpeWVuIGRl"
    "IGF5bsSxIGxhbWJhbsSxbiBtZW11cnVkdXIuIEFzxLFsIGlrdGlkYXIsIMSxxZ/EscSf"
    "xLFuIHPDvHJlc2luaSBheWFybGF5YW4gcGFub251biBpw6dpbmRlZGlyLg=="
)


def evrak_no(hiz: float, mesafe: float, saniye: float) -> str:
    ham = f"{hiz:.2f}|{mesafe:.2f}|{saniye:.2f}|sari".encode()
    ozet = hashlib.sha256(ham).hexdigest()[:8].upper()
    return f"SKD-2026-{ozet}"


def karar_ver(hiz_kmh: float, mesafe_m: float, sari_saniye: float) -> dict:
    if hiz_kmh < 0 or mesafe_m < 0 or sari_saniye < 0:
        raise ValueError("Negatif deger daireye giremez. Geri vites ayri birimdir.")

    hiz_ms = hiz_kmh / 3.6
    varis = mesafe_m / hiz_ms if hiz_ms > 0.3 else 999.0
    fren_mesafesi = (hiz_kmh / 10) ** 2  # uydurma ama tutarli okul formulu

    if mesafe_m < 4 and hiz_kmh > 30:
        hukum = "GEC"
        gerekce = "Durmak artik fizik degil, tiyatro olur. Daire tiyatroyu sever ama kavsak sevmez."
    elif varis <= sari_saniye * 0.85 and mesafe_m > fren_mesafesi * 0.4:
        hukum = "GEC"
        gerekce = "Sari bitmeden cizgiyi gecme ihtimali, vicdaninizdan daha yuksek."
    elif fren_mesafesi > mesafe_m * 1.3:
        hukum = "FREN YARIM, PISMANLIK TAM"
        gerekce = "Ne durabildiniz ne gectiniz. Bu, memuriyetin saf halidir."
    elif sari_saniye >= 2.5 and mesafe_m > 15:
        hukum = "DUR"
        gerekce = "Sari size vakit verdi. Vakti reddetmek ayri bir dosyadir."
    else:
        hukum = "AYNAYA BAK, KARARI BASINA YIK"
        gerekce = "Arkadaki arac korna calarsa suclu siz, calmazsa suclu yine siz."

    sikayet = min(99, int(hiz_kmh * 0.7 + max(0, 20 - mesafe_m)))
    return {
        "hukum": hukum,
        "gerekce": gerekce,
        "varis": varis,
        "fren": fren_mesafesi,
        "sikayet": sikayet,
        "evrak": evrak_no(hiz_kmh, mesafe_m, sari_saniye),
    }


def tutanak(hiz: float, mesafe: float, saniye: float) -> str:
    k = karar_ver(hiz, mesafe, saniye)
    govde = textwrap.fill(k["gerekce"], width=68)
    return (
        "========================================\n"
        " SARI ISIK KARARSIZLIK DAIRESI\n"
        " TUTANAK / SARARMAMIS NUSHADIR\n"
        "========================================\n"
        f"Evrak   : {k['evrak']}\n"
        f"Hiz     : {hiz:.1f} km/s\n"
        f"Mesafe  : {mesafe:.1f} m\n"
        f"Sari    : {saniye:.1f} sn\n"
        f"Varis   : {k['varis']:.2f} sn (teorik)\n"
        f"Fren    : {k['fren']:.1f} m (okul yalanlari)\n"
        f"Hukum   : {k['hukum']}\n"
        f"Sikayet : yuzde {k['sikayet']} (arkadaki serit)\n"
        "----------------------------------------\n"
        f"{govde}\n"
        "----------------------------------------\n"
        "Itiraz: ayni daire, farkli cay bardagi.\n"
        "Muhur kontrolu gecti. Icerik gizli, sonuc sari.\n"
    )


def _sayi_iste(yazi: str, varsayilan: float) -> float:
    ham = input(f"{yazi} [{varsayilan}]: ").strip().replace(",", ".")
    if not ham:
        return varsayilan
    return float(ham)


def main() -> None:
    print("Sari Isik Kararsizlik Dairesi acildi. Sira sizde, lamba degil.")
    print("Bos birakirsaniz ornek dosya islenir.\n")
    try:
        hiz = _sayi_iste("Hiz (km/s)", 48)
        mesafe = _sayi_iste("Kavsaga mesafe (metre)", 22)
        saniye = _sayi_iste("Sari kalan omur (saniye)", 1.4)
        print()
        print(tutanak(hiz, mesafe, saniye))
    except ValueError as hata:
        print(f"Evrak iade: {hata}")
        return
    random.seed(int(hiz + mesafe))
    dipnot = random.choice(
        [
            "Korna bir gorus belirtmez, sadece ses olur.",
            "Yesil de sarinin emekli halidir.",
            "Kirmizi su an izindedir. Dosyayi karistirmayin.",
        ]
    )
    print(dipnot)
    print("Damga: Kayyum Grok / 7 Ekim 2026 / ciddidir, gulumsemesi yasaktir ama kacar.")


if __name__ == "__main__":
    main()
