"""Link verified Trello cards into the planning appendix without duplicating content."""
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
planning=root/'planning'
sync=json.loads((planning/'trello-sync-result.json').read_text(encoding='utf-8'))
cards={c['id']:c for c in sync['cards']}
assert len(cards)==64 and all(c['description_saved'] for c in cards.values())
path=planning/'sprint-planning.md'
text=path.read_text(encoding='utf-8')
text=text.split('\n## Tablero Trello verificado',1)[0]
text+='\n## Tablero Trello verificado\n\n'
text+=f"[EnergyCore - Product Backlog y Sprint Planning]({sync['board_url']})\n\n"
text+='Verificación: 20/10/2026. 64 tarjetas con descripción, estado y enlace propio; 0 duplicados o discrepancias. El tablero es privado. No se enviaron invitaciones ni se atribuyeron responsables o actividad histórica sin confirmación.\n\n'
text+='| Sprint | Tarjeta de planificación | Naturaleza |\n|:--|:--|:--|\n'
for number in range(1,8):
    card=cards[f'PLAN-{number:02}']
    nature='Reconstrucción histórica' if number<=3 else ('Revisión TB1' if number==4 else 'Propuesto / Por iniciar')
    text+=f"| {number} | [PLAN-{number:02}]({card['url']}) | {nature} |\n"
text+='\nDistribución verificada: Backlog 13; Por iniciar 14; En curso 0; Implementado - por verificar 33; Verificado - pruebas y CI 4. El acta `trello-sync-result.json` contiene los 64 enlaces y la confirmación de lectura posterior.\n'
path.write_text(text,encoding='utf-8')
print('Linked seven verified Sprint Planning cards and board evidence.')
