#Faça um programa em python que abra e reproduza o áudio de um 
#arquivo mp3.
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Exercícios/musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()



