import matplotlib.pyplot as plt
c = 3.0e5  
H0 = 70.0  
z_list = []
D_list = []
print("Cosmic Redshift & Distance Tracker")
print("-------------------------------------")
while True:
    while True:
        try:
            lambda_emit = float(input("\nEnter emitted wavelength (λ_emit) in nm: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    while True:
        try:
            lambda_obs = float(input("Enter observed wavelength (λ_obs) in nm: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    z = (lambda_obs - lambda_emit) / lambda_emit
    D = (c * z) / H0       
    D_ly = D * 3.26        
    z_list.append(z)
    D_list.append(D)
    print("\nResults:")
    print(f"Redshift (z): {z:.5f}")
    print(f"Approximate Distance: {D:.2f} Mpc ({D_ly:.2f} million light years)")
    if z < 0:
        print("→ The object is moving toward us (blueshift).")
    elif z < 0.01:
        print("→ Very nearby galaxy (Local Group scale).")
    elif z < 0.1:
        print("→ Relatively close galaxy.")
    elif z < 1:
        print("→ Distant galaxy or quasar.")
    else:
        print("→ Very distant object (early universe epoch).")
    while True:
        print("\nWhat would you like to do next?")
        print("1 → New calculation")
        print("2 → Show all measurements on graph")
        print("3 → Exit program")
        next_action = input("Select (1, 2, or 3): ")
        if next_action == "1":
            break 
        elif next_action == "2":
            plt.figure(figsize=(8,5))
            plt.plot(z_list, D_list, 'o-', linewidth=2, markersize=6)
            plt.title("Cosmic Redshift vs Distance")
            plt.xlabel("Redshift (z)")
            plt.ylabel("Distance (Mpc)")
            plt.grid(True)
            plt.show()
            while True:
                print("\nGraph Options:")
                print("1 → Reopen graph")
                print("2 → New calculation")
                print("3 → Exit program")
                graph_choice = input("Select (1, 2, or 3): ")
                if graph_choice == "1":
                    plt.figure(figsize=(8,5))
                    plt.plot(z_list, D_list, 'o-', linewidth=2, markersize=6)
                    plt.title("Cosmic Redshift vs Distance")
                    plt.xlabel("Redshift (z)")
                    plt.ylabel("Distance (Mpc)")
                    plt.grid(True)
                    plt.show()
                elif graph_choice == "2":
                    break 
                elif graph_choice == "3":
                    print("Exiting program.")
                    exit()
                else:
                    print("Invalid choice! Please enter 1, 2, or 3.")
            break  
        elif next_action == "3":
            print("Exiting program.")
            exit()
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
