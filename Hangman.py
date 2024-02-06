import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und Farben
breite, höhe = 800, 600
hintergrundfarbe = (255, 255, 255)
button_farbe = (50, 150, 255)

# Einrichtung des Fensters
screen = pygame.display.set_mode((breite, höhe))
pygame.display.set_caption("Hangman Spiel")

# Funktion zum Starten des Spiels
def starte_spiel(schwierigkeit):
    # Hier kannst du den Code für das Hangman-Spiel hinzufügen
    print(f"Spiel gestartet mit Schwierigkeitsgrad: {schwierigkeit}")
    if schwierigkeit == "Leicht":
        spiel_leicht()
    elif schwierigkeit == "Mittel":
        spiel_mittel()
    elif schwierigkeit == "Schwer":
        spiel_schwer()



# Funktion zum Beenden des Programms
def beende_spiel():
    pygame.quit()
    sys.exit()

# Hauptfunktion für die GUI
def hauptmenü():
    schwierigkeitsstufen = ["Leicht", "Mittel", "Schwer"]
    aktuelle_schwierigkeit_index = 0

    while True:
        screen.fill(hintergrundfarbe)

        # Hangman-Logo
        schriftart = pygame.font.Font(None, 100)
        logo_text = schriftart.render("Hangman", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        # Schwierigkeitsgrad-Text
        schwierigkeits_text = schriftart.render(schwierigkeitsstufen[aktuelle_schwierigkeit_index], True, (0, 0, 0))
        schwierigkeits_rechteck = schwierigkeits_text.get_rect(center=(breite // 2, höhe // 2))
        screen.blit(schwierigkeits_text, schwierigkeits_rechteck)

        # Leicht Text
        schriftart_leicht = pygame.font.Font(None, 70)
        leicht_text = schriftart_leicht.render("Leicht", True, (0, 0, 0))
        leicht_rechteck = leicht_text.get_rect(center=(200, 400))
        screen.blit(leicht_text, leicht_rechteck)

        # Mittel Text
        schriftart_mittel = pygame.font.Font(None, 70)
        mittel_text = schriftart_mittel.render("Mittel", True, (0, 0, 0))
        mittel_rechteck = mittel_text.get_rect(center=(400, 400))
        screen.blit(mittel_text, mittel_rechteck)

        # Schwer Text
        schriftart_schwer = pygame.font.Font(None, 70)
        schwer_text = schriftart_schwer.render("Schwer", True, (0, 0, 0))
        schwer_rechteck = schwer_text.get_rect(center=(600, 400))
        screen.blit(schwer_text, schwer_rechteck)

        # Button für Starten
        start_button = pygame.Rect(breite // 2 - 100, höhe // 2 + 200, 200, 50)
        pygame.draw.rect(screen, button_farbe, start_button)
        start_text = schriftart.render("Starten", True, (0, 0, 0))
        start_rechteck = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rechteck)

        # Aktualisiere den Bildschirm
        pygame.display.flip()

        # Event-Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                maus_position = pygame.mouse.get_pos()
                
                # Überprüfe, ob auf "Leicht", "Mittel" oder "Schwer" geklickt wurde
                if leicht_rechteck.collidepoint(maus_position):
                    aktuelle_schwierigkeit_index = 0
                elif mittel_rechteck.collidepoint(maus_position):
                    aktuelle_schwierigkeit_index = 1
                elif schwer_rechteck.collidepoint(maus_position):
                    aktuelle_schwierigkeit_index = 2
                elif start_button.collidepoint(maus_position):
                    starte_spiel(schwierigkeitsstufen[aktuelle_schwierigkeit_index])

def spiel_leicht():

    screen = pygame.display.set_mode((800, 600))

    while True:
        screen.fill((80, 255, 90))

        schriftart = pygame.font.Font(None, 80)
        logo_text = schriftart.render("Leicht", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()

def spiel_mittel():

    screen = pygame.display.set_mode((800, 600))

    while True:
        screen.fill((255, 200, 70))

        schriftart = pygame.font.Font(None, 80)
        logo_text = schriftart.render("Mittel", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()

def spiel_schwer():

    screen = pygame.display.set_mode((800, 600))

    while True:
        screen.fill((255, 70 ,110))

        schriftart = pygame.font.Font(None, 80)
        logo_text = schriftart.render("Schwer", True, (0, 0, 0))
        logo_rechteck = logo_text.get_rect(center=(breite // 2, höhe // 4))
        screen.blit(logo_text, logo_rechteck)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beende_spiel()


# Starte die GUI
hauptmenü()

