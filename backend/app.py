from src import app
from src.config.api_registers import main


if __name__ == '__main__':
    main()
    app.run(debug=True)
