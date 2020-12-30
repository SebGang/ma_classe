from maclasse import app, setup_database


if __name__ == "__main__":
    setup_database()
    # setup_routes(app)

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
