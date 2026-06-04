from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola Mundo Flask</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
        }

        .card{
            background:white;
            padding:40px;
            border-radius:20px;
            box-shadow:0 10px 30px rgba(0,0,0,0.2);
            text-align:center;
            width:400px;
            animation: aparecer 1s ease;
        }

        h1{
            color:#333;
            margin-bottom:15px;
            font-size:40px;
        }

        p{
            color:#666;
            font-size:18px;
            margin-bottom:25px;
        }

        .btn{
            display:inline-block;
            padding:12px 25px;
            background:#4facfe;
            color:white;
            text-decoration:none;
            border-radius:10px;
            transition:0.3s;
            font-weight:bold;
        }

        .btn:hover{
            background:#0077ff;
            transform:scale(1.05);
        }

        @keyframes aparecer{
            from{
                opacity:0;
                transform:translateY(20px);
            }
            to{
                opacity:1;
                transform:translateY(0);
            }
        }
    </style>
</head>
<body>

    <div class="card">
        <h1> Hola Mundo trabajo en clase </h1>
        <p>Ejercicio de git</p>
        <a href="/" class="btn">Recargar Página</a>
    </div>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )