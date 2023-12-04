import subprocess

def run_command(command):
    try:
        # Викликайте команду за допомогою Popen
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Очікуйте завершення процесу та отримайте вивід
        output, error = process.communicate()

        # Перевірте код виходу
        if process.returncode == 0:
            return {"output": output, "error": error, "success": True}
        else:
            return {"output": output, "error": error, "success": False, "exit_code": process.returncode}

    except Exception as e:
        return {"output": None, "error": str(e), "success": False}

# Приклад виклику функції
commands={
    'pwd':'echo %cd%',
    'ls':'dir'}
result = run_command()

# Виведення результатів
print("Output:", result["output"])
print("Error:", result["error"])
print("Success:", result["success"])

if not result["success"]:
    print("Exit Code:", result["exit_code"])