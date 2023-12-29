from flask import Flask, request, jsonify
import json

app = Flask(__name__)

monsters_data = {
    'monsters': [
                    {"id": 1,   "Name": "Devil Troop of Desire",                          "Area": "D1",                     "Room": 1,     "Level": 46,      "HP": 9100,       "EXP": 3500},
                    {"id": 2,   "Name": "Doggebi of   Name Face",                         "Area": "D1",                     "Room": 1,     "Level": 46,      "HP": 9100,       "EXP": 3500},
                    {"id": 3,   "Name": "Doggebi with a Gong",                            "Area": "D1",                     "Room": 5,     "Level": 46,      "HP": 9100,       "EXP": 3500},
                    {"id": 4,   "Name": "Drunken Doggebi",                                "Area": "D1",                     "Room": 1,     "Level": 47,      "HP": 9500,       "EXP": 4000},
                    {"id": 5,   "Name": "Devil Troop of Pain",                            "Area": "D1",                     "Room": 5,     "Level": 47,      "HP": 9500,       "EXP": 4000},
                    {"id": 6,   "Name": "Doggebi with a Mask of Black Crow",              "Area": "D1",                     "Room": 5,     "Level": 48,      "HP": 9800,       "EXP": 4700},
                    {"id": 7,   "Name": "Devil Troop of Jealousy",                        "Area": "D1",                     "Room": 3,     "Level": 48,      "HP": 9800,       "EXP": 4700},
                    {"id": 8,   "Name": "Devil Troop of Hatred",                          "Area": "D1",                     "Room": 5,     "Level": 48,      "HP": 9800,       "EXP": 4700},
                    {"id": 9,   "Name": "Giant Doggebi",                                  "Area": "D1",                     "Room": 9,     "Level": 49,      "HP": 10000,      "EXP": 5400},
                    {"id": 10,  "Name": "Devil Troop of Madness",                         "Area": "D1",                     "Room": 9,     "Level": 49,      "HP": 10000,      "EXP": 5400},
                    {"id": 11,  "Name": "Guardian of Doggebi",                            "Area": "D1",                     "Room": 9,     "Level": 50,      "HP": 11000,      "EXP": 6300},
                    {"id": 12,  "Name": "Devil Troop of Anger",                           "Area": "D1",                     "Room": 9,     "Level": 50,      "HP": 11000,      "EXP": 6300},
                    {"id": 13,  "Name": "Minister of the Royal Tomb",                     "Area": "D2",       "Hall": 1,    "Room": 1,     "Level": 61,      "HP": 16000,      "EXP": 34000},
                    {"id": 14,  "Name": "The Royal Tomb Keeper",                          "Area": "D2",       "Hall": 1,    "Room": 1,     "Level": 62,      "HP": 17000,      "EXP": 39000},
                    {"id": 15,  "Name": "The Royal Tomb Keeper",                          "Area": "D2",       "Hall": 1,    "Room": 0,     "Level": 63,      "HP": 18000,      "EXP": 46000},
                    {"id": 16,  "Name": "The Royal Tomb Keeper",                          "Area": "D2",       "Hall": 1,    "Room": 0,     "Level": 64,      "HP": 18000,      "EXP": 54000},
                    {"id": 17,  "Name": "The Royal Tomb Keeper",                          "Area": "D2",       "Hall": 1,    "Room": 0,     "Level": 65,      "HP": 19000,      "EXP": 64000},
                    {"id": 18,  "Name": "Warrior of Shadow Troop",                        "Area": "D2",       "Hall": 2,    "Room": 9,     "Level": 66,      "HP": 20000,      "EXP": 75000},
                    {"id": 19,  "Name": "Hook of Shadow Troop",                           "Area": "D2",       "Hall": 2,    "Room": 4,     "Level": 67,      "HP": 21000,      "EXP": 89000},
                    {"id": 20,  "Name": "Watcher of Shadow Troop",                        "Area": "D2",       "Hall": 2,    "Room": 3,     "Level": 68,      "HP": 22000,      "EXP": 110000},
                    {"id": 21,  "Name": "Chief Warrior of Shadow Troop",                  "Area": "D2",       "Hall": 3,    "Room": 1,     "Level": 69,      "HP": 23000,      "EXP": 130000},
                    {"id": 22,  "Name": "Spear Hand of Shadow Troop",                     "Area": "D2",       "Hall": 3,    "Room": 2,     "Level": 70,      "HP": 24000,      "EXP": 150000},
                    {"id": 23,  "Name": "1st Commander of The Royal Tomb",                "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000},
                    {"id": 24,  "Name": "2nd Commander of The Royal Tomb",                "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000},
                    {"id": 25,  "Name": "3rd Commander of The Royal Tomb",                "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000},
                    {"id": 26,  "Name": "Chief Escort of The Royal Tomb",                 "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000},
                    {"id": 27,  "Name": "Chief Guard of The Royal Tomb",                  "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000},
                    {"id": 28,  "Name": "Imperial Commander of The Royal Tomb",           "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000},
                    {"id": 29,  "Name": "Lord of Shadow Troop",                           "Area": "D2",       "Hall": 3,    "Room": 4,     "Level": 70,      "HP": 440000,     "EXP": 150000}, 
                    {"id": 30,  "Name": "High Class Doggebi of  Name Face",               "Area": "D3",       "Floor": 1,                  "Level": 51,      "HP": 11000,      "EXP": 7300},
                    {"id": 31,  "Name": "High Class Doggebi with a Gong",                 "Area": "D3",       "Floor": 1,                  "Level": 51,      "HP": 11000,      "EXP": 7300},
                    {"id": 32,  "Name": "High Class Drunken Doggebi",                     "Area": "D3",       "Floor": 1,                  "Level": 51,      "HP": 11000,      "EXP": 7300},
                    {"id": 33,  "Name": "High Class Doggebi with a Mask of Black Crow",   "Area": "D3",       "Floor": 1,                  "Level": 52,      "HP": 11000,      "EXP": 8400},
                    {"id": 34,  "Name": "High Class Drunken Doggebi",                     "Area": "D3",       "Floor": 1,                  "Level": 53,      "HP": 12000,      "EXP": 9800},
                    {"id": 35,  "Name": "Chief of Demon Crack Troop",                     "Area": "D3",       "Floor": 2,                  "Level": 54,      "HP": 12000,      "EXP": 11000},
                    {"id": 36,  "Name": "Demon Crack Soldier",                            "Area": "D3",       "Floor": 2,                  "Level": 54,      "HP": 12000,      "EXP": 11000},
                    {"id": 37,  "Name": "Name of Demon Crack Troop",                      "Area": "D3",       "Floor": 2,                  "Level": 54,      "HP": 12000,      "EXP": 11000},
                    {"id": 38,  "Name": "White Beast of Demon Crack Troop",               "Area": "D3",       "Floor": 3,                  "Level": 57,      "HP": 14000,      "EXP": 18000},
                    {"id": 39,  "Name": "Blue Beast of Demon Crack Troop",                "Area": "D3",       "Floor": 3,                  "Level": 57,      "HP": 14000,      "EXP": 18000},
                    {"id": 40,  "Name": "Punitive Force of Demon Crack Troop",            "Area": "D3",       "Floor": 3,                  "Level": 58,      "HP": 14000,      "EXP": 21000},
                    {"id": 41,  "Name": "Hermit of White Beard",                          "Area": "D3",       "Floor": 4,                  "Level": 71,      "HP": 26000,      "EXP": 180000},
                    {"id": 42,  "Name": "Hermit of Long Beard",                           "Area": "D3",       "Floor": 4,                  "Level": 72,      "HP": 27000,      "EXP": 210000},
                    {"id": 43,  "Name": "Hermit of Red Face",                             "Area": "D3",       "Floor": 4,                  "Level": 73,      "HP": 28000,      "EXP": 250000},
                    {"id": 44,  "Name": "Hermit of White Beard",                          "Area": "D3",       "Floor": 5,                  "Level": 74,      "HP": 30000,      "EXP": 300000},
                    {"id": 45,  "Name": "Hermit of Mask",                                 "Area": "D3",       "Floor": 5,                  "Level": 75,      "HP": 31000,      "EXP": 360000},
                    {"id": 46,  "Name": "Tough Hermit",                                   "Area": "D3",       "Floor": 5,                  "Level": 76,      "HP": 33000,      "EXP": 430000},
                    {"id": 47,  "Name": "Hermit of Mask",                                 "Area": "D3",       "Floor": 6,                  "Level": 77,      "HP": 35000,      "EXP": 510000},
                    {"id": 48,  "Name": "Hermit of Red Face",                             "Area": "D3",       "Floor": 6,                  "Level": 77,      "HP": 35000,      "EXP": 510000},
                    {"id": 49,  "Name": "Hermit of Anger",                                "Area": "D3",       "Floor": 6,                  "Level": 78,      "HP": 36000,      "EXP": 610000},
                    {"id": 50,  "Name": "Tough Hermit",                                   "Area": "D3",       "Floor": 6,                  "Level": 78,      "HP": 36000,      "EXP": 610000},
                    {"id": 51,  "Name": "Hermit of Anger",                                "Area": "D3",       "Floor": 7,                  "Level": 79,      "HP": 38000,      "EXP": 730000},
                    {"id": 52,  "Name": "High Class Giant Doggebi",                       "Area": "D3",       "Floor": 7,                  "Level": 79,      "HP": 38000,      "EXP": 730000},
                    {"id": 53,  "Name": "High Class Doggebi with a Mask of Black Panther","Area": "D3",       "Floor": 8,                  "Level": 79,      "HP": 38000,      "EXP": 730000},
                    {"id": 54,  "Name": "Tough Hermit",                                   "Area": "D3",       "Floor": 8,                  "Level": 79,      "HP": 38000,      "EXP": 730000},
                    {"id": 55,  "Name": "High Class Guardian of Doggebi",                 "Area": "D3",       "Floor": 8,                  "Level": 80,      "HP": 40000,      "EXP": 880000},
                    {"id": 56,  "Name": "Hermit of Anger",                                "Area": "D3",       "Floor": 9,                  "Level": 76,      "HP": 33000,      "EXP": 430000},
                    {"id": 57,  "Name": "Demon Worker",                                   "Area": "D4",       "Floor": 1,                  "Level": 50,      "HP": 11000,      "EXP": 6300},
                    {"id": 58,  "Name": "Demon Guard",                                    "Area": "D4",       "Floor": 2,                  "Level": 65,      "HP": 19000,      "EXP": 64000},
                    {"id": 59,  "Name": "Larva",                                          "Area": "D4",       "Floor": 4,                  "Level": 70,      "HP": 24000,      "EXP": 150000},
                    {"id": 60,  "Name": "Demon Patrol",                                   "Area": "D4",       "Floor": 3,                  "Level": 70,      "HP": 24000,      "EXP": 150000},
                    {"id": 61,  "Name": "Black Armored Insect",                           "Area": "D4",       "Floor": 4,                  "Level": 70,      "HP": 24000,      "EXP": 150000},
                    {"id": 62,  "Name": "Demon Warrior",                                  "Area": "D4",       "Floor": 4,                  "Level": 73,      "HP": 28000,      "EXP": 250000},
                    {"id": 63,  "Name": "Demon Infantry",                                 "Area": "D4",       "Floor": 5,                  "Level": 75,      "HP": 31000,      "EXP": 360000},
                    {"id": 64,  "Name": "Crazy Demon Warrior",                            "Area": "D4",       "Floor": 5,                  "Level": 78,      "HP": 36000,      "EXP": 610000},
                    {"id": 65,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 1,                  "Level": 81,      "HP": 43000,      "EXP": 1100000},
                    {"id": 66,  "Name": "Skeleton",                                       "Area": "D5",       "Floor": 1,                  "Level": 81,      "HP": 43000,      "EXP": 1100000},
                    {"id": 67,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 1,                  "Level": 81,      "HP": 43000,      "EXP": 1100000},
                    {"id": 68,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 2,                  "Level": 82,      "HP": 45000,      "EXP": 1300000},
                    {"id": 69,  "Name": "Skeleton",                                       "Area": "D5",       "Floor": 2,                  "Level": 82,      "HP": 45000,      "EXP": 1300000},
                    {"id": 70,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 2,                  "Level": 82,      "HP": 45000,      "EXP": 1300000},
                    {"id": 71,  "Name": "Elite Skeleton",                                 "Area": "D5",       "Floor": 2,                  "Level": 82,      "HP": 45000,      "EXP": 1300000},
                    {"id": 72,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 3,                  "Level": 83,      "HP": 48000,      "EXP": 1500000},
                    {"id": 73,  "Name": "Skeleton",                                       "Area": "D5",       "Floor": 3,                  "Level": 83,      "HP": 48000,      "EXP": 1500000},
                    {"id": 74,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 3,                  "Level": 83,      "HP": 48000,      "EXP": 1500000},
                    {"id": 75,  "Name": "Elite Skeleton",                                 "Area": "D5",       "Floor": 3,                  "Level": 83,      "HP": 48000,      "EXP": 1500000},
                    {"id": 76,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 3,                  "Level": 84,      "HP": 51000,      "EXP": 1700000},
                    {"id": 77,  "Name": "Skeleton Warrior",                               "Area": "D5",       "Floor": 3,                  "Level": 84,      "HP": 51000,      "EXP": 1700000},
                    {"id": 78,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 3,                  "Level": 84,      "HP": 51000,      "EXP": 1700000},
                    {"id": 79,  "Name": "Elite Skeleton",                                 "Area": "D5",       "Floor": 2,                  "Level": 84,      "HP": 51000,      "EXP": 1700000},
                    {"id": 80,  "Name": "Elite Skeleton",                                 "Area": "D5",       "Floor": 4,                  "Level": 84,      "HP": 51000,      "EXP": 1700000},
                    {"id": 81,  "Name": "Wraith",                                         "Area": "D5",       "Floor": 4,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 82,  "Name": "Skeleton Warrior",                               "Area": "D5",       "Floor": 4,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 83,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 4,                  "Level": 83,      "HP": 48000,      "EXP": 1500000},
                    {"id": 84,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 4,                  "Level": 84,      "HP": 51000,      "EXP": 1700000},
                    {"id": 85,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 4,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 86,  "Name": "Skeleton Warrior",                               "Area": "D5",       "Floor": 5,                  "Level": 86,      "HP": 57000,      "EXP": 2200000},
                    {"id": 87,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 5,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 88,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 5,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 89,  "Name": "Elite Skeleton",                                 "Area": "D5",       "Floor": 5,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 90,  "Name": "Wraith",                                         "Area": "D5",       "Floor": 5,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 91,  "Name": "Skeleton Warrior",                               "Area": "D5",       "Floor": 6,                  "Level": 86,      "HP": 57000,      "EXP": 2200000},
                    {"id": 92,  "Name": "Banshee",                                        "Area": "D5",       "Floor": 6,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 93,  "Name": "Skeleton Archer",                                "Area": "D5",       "Floor": 6,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 94,  "Name": "Elite Skeleton",                                 "Area": "D5",       "Floor": 6,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 95,  "Name": "Wraith",                                         "Area": "D5",       "Floor": 6,                  "Level": 85,      "HP": 54000,      "EXP": 1900000},
                    {"id": 96,  "Name": "High Class Fire element",                        "Area": "D5",       "Floor": 7,                  "Level": 92,      "HP": 82000,      "EXP": 4800000},
                    {"id": 97,  "Name": "High Class Water element",                       "Area": "D5",       "Floor": 7,                  "Level": 92,      "HP": 82000,      "EXP": 4800000},
                    {"id": 98,  "Name": "High Class Earth element",                       "Area": "D5",       "Floor": 7,                  "Level": 92,      "HP": 82000,      "EXP": 4800000},
                    {"id": 99,  "Name": "High Class Wood element",                        "Area": "D5",       "Floor": 7,                  "Level": 92,      "HP": 82000,      "EXP": 4800000},
                    {"id": 100, "Name": "High Class Iron element",                        "Area": "D5",       "Floor": 7,                  "Level": 92,      "HP": 82000,      "EXP": 4800000},
                    {"id": 101, "Name": "Wraith",                                         "Area": "D5",       "Floor": 7,                  "Level": 86,      "HP": 57000,      "EXP": 2200000},
                    {"id": 102, "Name": "High Class Security guard of the priest",        "Area": "D5",       "Floor": 7,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 103, "Name": "High Class Wood element",                        "Area": "D5",       "Floor": 8,                  "Level": 93,      "HP": 87000,      "EXP": 5400000},
                    {"id": 104, "Name": "High Class Iron element",                        "Area": "D5",       "Floor": 8,                  "Level": 93,      "HP": 87000,      "EXP": 5400000},
                    {"id": 105, "Name": "Security guard of the priest",                   "Area": "D5",       "Floor": 8,                  "Level": 93,      "HP": 87000,      "EXP": 5400000},
                    {"id": 106, "Name": "High Class Fire element",                        "Area": "D5",       "Floor": 8,                  "Level": 93,      "HP": 87000,      "EXP": 5400000},
                    {"id": 107, "Name": "High Class Earth element",                       "Area": "D5",       "Floor": 8,                  "Level": 93,      "HP": 87000,      "EXP": 5400000},
                    {"id": 108, "Name": "High Class Water element",                       "Area": "D5",       "Floor": 8,                  "Level": 93,      "HP": 87000,      "EXP": 5400000},
                    {"id": 109, "Name": "High Class Security guard of the priest",        "Area": "D5",       "Floor": 8,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 110, "Name": "Wraith",                                         "Area": "D5",       "Floor": 8,                  "Level": 86,      "HP": 57000,      "EXP": 2200000},
                    {"id": 111, "Name": "High Class Iron element",                        "Area": "D5",       "Floor": 9,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 112, "Name": "High Class Wood element",                        "Area": "D5",       "Floor": 9,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 113, "Name": "High Class Water element",                       "Area": "D5",       "Floor": 9,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 114, "Name": "High Class Earth element",                       "Area": "D5",       "Floor": 9,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 115, "Name": "High Class Fire element",                        "Area": "D5",       "Floor": 9,                  "Level": 94,      "HP": 92000,      "EXP": 6200000},
                    {"id": 116, "Name": "High Class Security guard of the priest",        "Area": "D5",       "Floor": 9,                  "Level": 95,      "HP": 98000,      "EXP": 7100000},
                    {"id": 117, "Name": "Wraith",                                         "Area": "D5",       "Floor": 9,                  "Level": 87,      "HP": 61000,      "EXP": 2500000},
                    {"id": 118, "Name": "Dungeon Warrior",                                "Area": "D6",       "Floor": 1,                  "Level": 117,     "HP": 440000,     "EXP": 350000000},
                    {"id": 119, "Name": "Dungeon Scout Soldier",                          "Area": "D6",       "Floor": 1,                  "Level": 119,     "HP": 490000,     "EXP": 440000000},
                    {"id": 120, "Name": "Dungeon Shield Soldier",                         "Area": "D6",       "Floor": 1,                  "Level": 118,     "HP": 460000,     "EXP": 390000000},
                    {"id": 121, "Name": "Dungeon Warrior",                                "Area": "D6",       "Floor": 2,                  "Level": 120,     "HP": 520000,     "EXP": 490000000},
                    {"id": 122, "Name": "Dungeon Scout Soldier",                          "Area": "D6",       "Floor": 2,                  "Level": 120,     "HP": 520000,     "EXP": 490000000},
                    {"id": 123, "Name": "Elite Dungeon Warrior",                          "Area": "D6",       "Floor": 2,                  "Level": 122,     "HP": 580000,     "EXP": 620000000},
                    {"id": 124, "Name": "Elite Dungeon Scout Soldier",                    "Area": "D6",       "Floor": 2,                  "Level": 122,     "HP": 580000,     "EXP": 620000000},
                    {"id": 125, "Name": "Elite Dungeon Shield Soldier",                   "Area": "D6",       "Floor": 2,                  "Level": 122,     "HP": 580000,     "EXP": 620000000},
                    {"id": 126, "Name": "Dungeon Guard",                                  "Area": "D6",       "Floor": 2,                  "Level": 121,     "HP": 550000,     "EXP": 550000000},
                    {"id": 127, "Name": "Elite Dungeon Guard",                            "Area": "D6",       "Floor": 2,                  "Level": 122,     "HP": 580000,     "EXP": 620000000},
                    {"id": 128, "Name": "Dungeon Shock Trooper",                          "Area": "D6",       "Floor": 2,                  "Level": 121,     "HP": 550000,     "EXP": 550000000},
                    {"id": 129, "Name": "Elite Dungeon Shock Trooper",                    "Area": "D6",       "Floor": 2,                  "Level": 122,     "HP": 580000,     "EXP": 620000000},
                    {"id": 130, "Name": "Dungeon Ax Soldier",                             "Area": "D6",       "Floor": 2,                  "Level": 121,     "HP": 550000,     "EXP": 550000000},
                    {"id": 131, "Name": "Elite Dungeon Ax Soldier",                       "Area": "D6",       "Floor": 2,                  "Level": 122,     "HP": 580000,     "EXP": 620000000},
                    {"id": 132, "Name": "Ruins Destroyer (Water)",                        "Area": "D6",       "Floor": "2.5",              "Level": 123,     "HP": 620000,     "EXP": 690000000},
                    {"id": 133, "Name": "Dungeon Magician",                               "Area": "D6",       "Floor": "2.5",              "Level": 124,     "HP": 650000,     "EXP": 780000000},
                    {"id": 134, "Name": "Ohgeuma (Wind)",                                 "Area": "D6",       "Floor": "2.5",              "Level": 124,     "HP": 650000,     "EXP": 780000000},
                    {"id": 135, "Name": "[Elite] Dungeon Knight",                         "Area": "D6",       "Floor": "2.5",              "Level": 126,     "HP": 730000,     "EXP": 970000000},
                    {"id": 136, "Name": "Lord Bisaim (Water)",                            "Area": "D6",       "Floor": "2.5",              "Level": 124,     "HP": 650000,     "EXP": 780000000},
                    {"id": 137, "Name": "Death Lich (Earth)",                             "Area": "D6",       "Floor": "2.5",              "Level": 124,     "HP": 650000,     "EXP": 780000000},
                    {"id": 138, "Name": "Death Knight (Earth)",                           "Area": "D6",       "Floor": "2.5",              "Level": 125,     "HP": 690000,     "EXP": 870000000},
                    {"id": 139, "Name": "Shadow Murder (Wind)",                           "Area": "D6",       "Floor": "2.5",              "Level": 123,     "HP": 620000,     "EXP": 690000000},
                    {"id": 140, "Name": "Elite Death Knight (Earth)",                     "Area": "D6",       "Floor": 3,                  "Level": 129,     "HP": 870000,     "EXP": 1.400000000},
                    {"id": 141, "Name": "Elite Ohgeuma (Wind)",                           "Area": "D6",       "Floor": 3,                  "Level": 128,     "HP": 820000,     "EXP": 1.200000000},
                    {"id": 142, "Name": "Elite Lord Bisaim (Water)",                      "Area": "D6",       "Floor": 3,                  "Level": 128,     "HP": 820000,     "EXP": 1.200000000},
                    {"id": 143, "Name": "Elite Death Lich (Earth)",                       "Area": "D6",       "Floor": 3,                  "Level": 128,     "HP": 820000,     "EXP": 1.200000000},
                    {"id": 144, "Name": "Elite Shadow Murder (Wind)",                     "Area": "D6",       "Floor": 3,                  "Level": 127,     "HP": 780000,     "EXP": 1.100000000},
                    {"id": 145, "Name": "Elite Ruins Destroyer (Water)",                  "Area": "D6",       "Floor": 3,                  "Level": 127,     "HP": 780000,     "EXP": 1.100000000},
                    {"id": 146, "Name": "Elite Death Harvester (Earth)",                  "Area": "D6",       "Floor": 3,                  "Level": 127,     "HP": 780000,     "EXP": 1.100000000},
                    {"id": 147, "Name": "[Elite] Dungeon Knight",                         "Area": "D6",       "Floor": 3,                  "Level": 130,     "HP": 920000,     "EXP": 1.500000000}
                    ]
                }

@app.route('/monsters', methods=['GET'])
def get_monsters():
    try:
        # Obtendo os níveis dos jogadores A e B a partir dos parâmetros da requisição
        player_a_level = int(request.args.get('player_a_level'))
        player_b_level = int(request.args.get('player_b_level'))

        # Calculando os limites para a pesquisa no array de monstros
        x = max(1, player_a_level - 9)
        y = player_b_level + 9

        # Filtrando e ordenando a lista de monstros com base nos limites calculados
        filtered_mobs = sorted(
            [
                {
                    'Name': mob['Name'],
                    'Area': mob['Area'],
                    'EXP': "{:,}".format(mob['EXP']).replace(',', '.'),
                    'Level': mob['Level']
                }
                for mob in monsters_data['monsters'] if x <= mob['Level'] <= y
            ],
            key=lambda x: x['Level']
        )

        return jsonify({'monsters': filtered_mobs})

    except ValueError:
        return jsonify({'error': 'Os níveis dos jogadores devem ser números inteiros.'}), 400

if __name__ == '__main__':
    app.run(debug=True)