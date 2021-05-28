from app import create_app,db

app = create_app()

db.create_all(app=create_app())


if __name__ == '__main__':
    
    app.run(debug=True)
    
    