from flask import Flask, render_template_string, jsonify
import os

app = Flask(__name__)

# HTML Template using Tailwind CSS for styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Primera App en Python + Render</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-white min-h-screen flex flex-col justify-between font-sans">
    
    <!-- Navbar -->
    <nav class="bg-slate-800 border-b border-slate-700 p-4">
        <div class="max-w-4xl mx-auto flex justify-between items-center">
            <h1 class="text-xl font-bold text-indigo-400">🐍 Python + Flask</h1>
            <span class="bg-emerald-500/10 text-emerald-400 text-xs px-2.5 py-1 rounded-full border border-emerald-500/20 font-mono">
                Status: Online
            </span>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto p-6 flex-grow flex flex-col justify-center items-center text-center">
        <div class="bg-slate-800/50 p-8 rounded-2xl border border-slate-700 shadow-xl max-w-lg w-full">
            <div class="inline-block p-4 bg-indigo-600/10 rounded-full text-indigo-400 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                </svg>
            </div>
            
            <h2 class="text-2xl font-bold mb-2 text-slate-100">¡Aplicación Lista para Desplegar!</h2>
            <p class="text-slate-400 text-sm mb-6">
                Esta es una aplicación backend escrita en Python con Flask, configurada específicamente para funcionar en Render.
            </p>

            <!-- Dynamic Server Info -->
            <div class="bg-slate-900/80 p-4 rounded-lg text-left text-xs font-mono mb-6 border border-slate-800 space-y-2">
                <div class="flex justify-between">
                    <span class="text-slate-500">Framework:</span>
                    <span class="text-slate-300">Flask 3.x</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-slate-500">Servidor Web:</span>
                    <span class="text-slate-300">Gunicorn</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-slate-500">Puerto Activo:</span>
                    <span class="text-indigo-400">{{ port }}</span>
                </div>
            </div>

            <a href="/api/info" class="inline-block w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-2.5 rounded-lg transition duration-200">
                Probar Endpoint JSON (/api/info)
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-800/40 border-t border-slate-800 py-4 text-center text-slate-500 text-xs">
        Desplegado en Render • Servidor Backend Python
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    # Detect port provided by Render's environment
    port = os.environ.get('PORT', '5000')
    return render_template_string(HTML_TEMPLATE, port=port)

@app.route('/api/info')
def api_info():
    # JSON API response example
    return jsonify({
        "status": "success",
        "message": "API Backend respondiendo correctamente desde la nube",
        "environment": "Render Cloud",
        "technologies": ["Python", "Flask", "Gunicorn"]
    })

if __name__ == '__main__':
    # Local development runner
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)