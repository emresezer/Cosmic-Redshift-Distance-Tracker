import matplotlib.pyplot as plt
c = 3.0e5 
H0 = 70.0  
z_list = []
D_list = []
print("🌌 Kızılya Kayma ve Uzaklık Takip Programı")
print("------------------------------------------")
while True:
    while True:
        try:
            lambda_emit = float(input("\nYayılan dalga boyunu girin (λ_emit) nm cinsinden: "))
            break
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")
    while True:
        try:
            lambda_obs = float(input("Gözlenen dalga boyunu girin (λ_obs) nm cinsinden: "))
            break
        except ValueError:
            print("Geçersiz giriş! Lütfen bir sayı girin.")
    z = (lambda_obs - lambda_emit) / lambda_emit
    D = (c * z) / H0
    D_ly = D * 3.26       
    z_list.append(z)
    D_list.append(D)
    print("\n🔭 Sonuçlar:")
    print(f"Kızılya Kayma (z): {z:.5f}")
    print(f"Yaklaşık Uzaklık: {D:.2f} Mpc ({D_ly:.2f} milyon ışık yılı)")
    if z < 0:
        print("→ Cisim bize doğru hareket ediyor (mavi kayma).")
    elif z < 0.01:
        print("→ Çok yakın galaksi (Yerel Grup ölçeğinde).")
    elif z < 0.1:
        print("→ Görece yakın galaksi.")
    elif z < 1:
        print("→ Uzak galaksi veya kuasar.")
    else:
        print("→ Çok uzak cisim (erken evren dönemi).")
    while True:
        print("\nSonraki adım ne olsun?")
        print("1 → Yeni hesaplama")
        print("2 → Tüm ölçümleri grafikte göster")
        print("3 → Programı kapat")
        next_action = input("Seçiminiz (1, 2 veya 3): ")
        if next_action == "1":
            break  
        elif next_action == "2":
            plt.figure(figsize=(8,5))
            plt.plot(z_list, D_list, 'o-', linewidth=2, markersize=6)
            plt.title("Kızılya Kayma vs Uzaklık")
            plt.xlabel("Kızılya Kayma (z)")
            plt.ylabel("Uzaklık (Mpc)")
            plt.grid(True)
            plt.show()
            while True:
                print("\nGrafik Seçenekleri:")
                print("1 → Grafiği tekrar aç")
                print("2 → Yeni hesaplama")
                print("3 → Programı kapat")
                graph_choice = input("Seçiminiz (1, 2 veya 3): ")
                if graph_choice == "1":
                    plt.figure(figsize=(8,5))
                    plt.plot(z_list, D_list, 'o-', linewidth=2, markersize=6)
                    plt.title("Kızılya Kayma vs Uzaklık")
                    plt.xlabel("Kızılya Kayma (z)")
                    plt.ylabel("Uzaklık (Mpc)")
                    plt.grid(True)
                    plt.show()
                elif graph_choice == "2":
                    break  
                elif graph_choice == "3":
                    print("Program kapatılıyor. Hoşçakalın")
                    exit()
                else:
                    print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")
            break
        elif next_action == "3":
            print("Program kapatılıyor. Hoşçakalın")
            exit()
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")
