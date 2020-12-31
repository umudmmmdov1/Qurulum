from rich.console import Console
from rich.panel import Panel
from rich.live_render import LiveRender
import sys
import os, shutil
console = Console()

def hata (text):
   console.print(text, style="bold red")
def bilgi (text):
   console.print(text, style="blue")
def basarili (text):
   console.print(f"[bold green]{text}[/]")
def onemli (text):
   console.print(text, style="bold cyan")
def soru (soru):
   return console.input(f"[bold yellow]{soru}[/]")
def logo (dil = "None"):
   surum = str(sys.version_info[0]) + "." + str(sys.version_info[1])
   console.print(Panel(f"[bold blue] U S Σ R Δ T O R ✔️ [/]\n\n[bold cyan]Version: [/][i]2.6[/]\n[bold cyan]Python: [/][i]{surum}[/]\n[bold cyan]Dil: [/][i]{dil}[/]"), justify="center")                         
def tamamlandi (saniye):
   console.print(Panel(f"[bold green]Qurulum başa çatdı!\n[i]Botu {round(saniye)} saniyə içində qurdunuz.[/]\n\n[bold green]Bir neçə dəqiqə sonra hər hansı bir söhbətdə .alive yazaraq botu test edə bilərsiz. Xoş işlətmələr :)[/]"), justify="center")                         
                   
def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)
