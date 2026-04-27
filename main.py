from src.ui.menu import iniciar_menu

## Entry point de la aplicación
def main():
   print("Iniciando sistema...")
   iniciar_menu()
   print("Sistema finalizado")

## Aseguramos que main solo se ejecute cuando el script es ejecutado directamente 
## Si importamos este archivo desde otro lado, NO se ejecuta automáticamente 
if __name__ == "__main__":
    main()
