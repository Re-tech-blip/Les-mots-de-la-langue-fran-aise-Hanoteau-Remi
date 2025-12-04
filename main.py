"""
Module d'analyse des mots de la langue française.
Contient des fonctions pour filtrer, rechercher et analyser des mots.
"""

# Importations et définition des variables globales
import random

# Définition des constantes (en majuscules, selon les conventions Python)
FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

# Fonctions secondaires

def read_data(file_path):
    """
    Lit un fichier et retourne une liste de mots, un mot par ligne.

    Args:
        file_path (str): Chemin vers le fichier.

    Returns:
        list: La liste des mots.

    >>> mots = read_data(FILENAME)
    >>> isinstance(mots, list)
    True
    >>> len(mots)
    336531
    >>> mots[1]
    'à'
    >>> mots[328570]
    'vaincre'
    >>> mots[290761]
    'sans'
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def ensemble_mots():
    """Retourne l'ensemble des mots contenus dans le fichier global FILENAME.

    Returns:
        set: L'ensemble des mots uniques.

    >>> mots = ensemble_mots()
    >>> isinstance(mots, set)
    True
    >>> len(mots)
    336531
    >>> "glomérules" in mots
    True
    >>> "glycosudrique" in mots
    False
    """
    return set(read_data(FILENAME))

def mots_de_n_lettres(mots, n):
    """Retourne le sous-ensemble des mots de n lettres.

    Args:
        mots (set): Ensemble de mots.
        n (int): Nombre de lettres.

    Returns:
        set: Sous-ensemble des mots de n lettres.

    >>> mots = ensemble_mots()
    >>> m15 = mots_de_n_lettres(mots, 15)
    >>> isinstance(m15, set)
    True
    >>> len(m15)
    8730
    >>> len(mots_de_n_lettres(mots, 23))
    4
    >>> sorted(list(mots_de_n_lettres(mots,24)))[0]
    'constitutionnalisassions'
    """
    return {mot for mot in mots if len(mot) == n}


def mots_avec(mots, s):
    """Retourne le sous-ensemble des mots incluant la chaîne de caractères s.

    Args:
        mots (set): Ensemble de mots.
        s (str): Chaîne de caractères à inclure.

    Returns:
        set: Sous-ensemble des mots incluant la chaîne s.

    >>> mots = ensemble_mots()
    >>> mk = mots_avec(mots, 'k')
    >>> isinstance(mk, set)
    True
    >>> len(mk)
    1621
    >>> 'ankyloseraient' in mk
    True
    >>> 'week-end' in mk
    True
    """
    return {mot for mot in mots if s in mot}


def cherche1(mots, start, stop, n):
    """Retourne le sous-ensemble des mots de n lettres commençant par start
    et finissant par stop.

    Args:
        mots (set): Ensemble de mots.
        start (str): Première chaîne (préfixe).
        stop (str): Dernière chaîne (suffixe).
        n (int): Nombre de lettres.

    Returns:
        set: Sous-ensemble des mots filtrés.

    >>> mots = ensemble_mots()
    >>> m_z = cherche1(mots, 'z', 'z', 7)
    >>> isinstance(m_z, set)
    True
    >>> len(m_z)
    10
    >>> sorted(list(m_z))[4:7]
    ['zinguez', 'zippiez', 'zonerez']
    """
    return {
        mot for mot in mots
        if len(mot) == n
        and mot.startswith(start)
        and mot.endswith(stop)
    }


def cherche2(mots, criteres):
    """Effectue une recherche complexe dans un ensemble de mots.

    Args:
        mots (set): Ensemble de mots.
        criteres (dict): Dictionnaire contenant les critères de recherche:
            lstart (list): liste des préfixes
            lmid (list): liste des chaînes de caractères intermédiaires
            lstop (list): liste des suffixes
            nmin (int): nombre de lettres minimum
            nmax (int): nombre de lettres maximum

    Returns:
        set: Sous-ensemble des mots correspondant aux critères.

    >>> mots = ensemble_mots()
    >>> criteres = {
    ...     'lstart': ['a'], 'lmid': ['b'], 'lstop': ['z'],
    ...     'nmin': 16, 'nmax': 16
    ... }
    >>> mab17ez = cherche2(mots, criteres)
    >>> isinstance(mab17ez, set)
    True
    >>> len(mab17ez)
    1
    >>> mab17ez
    {'alphabétisassiez'}
    """
    result = set()
    lstart = criteres['lstart']
    lmid = criteres['lmid']
    lstop = criteres['lstop']
    nmin = criteres['nmin']
    nmax = criteres['nmax']

    for mot in mots:
        # Vérifier la longueur (C0325 corrigé)
        if not (nmin <= len(mot) <= nmax):
            continue

        # Vérifier le préfixe
        prefix_ok = any(mot.startswith(prefix) for prefix in lstart)

        # Vérifier le suffixe
        suffix_ok = any(mot.endswith(suffix) for suffix in lstop)

        # Vérifier la chaîne intermédiaire
        mid_ok = any(mid in mot for mid in lmid)

        # Si toutes les conditions sont remplies
        if prefix_ok and suffix_ok and mid_ok:
            result.add(mot)
    return result


def main():
    """Fonction principale pour démontrer l'utilisation des fonctions."""
    # 1. Lire les données et créer l'ensemble de mots
    mots_liste = read_data(FILENAME)
    ens_mots = ensemble_mots()

    print("=== Analyse du corpus ===")
    print(f"Nombre total de mots : {len(mots_liste)}")
    print(f"Nombre de mots uniques : {len(ens_mots)}\n")

    # Définition des ensembles pour l'analyse
    mots_lettres = {
        'k': mots_avec(ens_mots, 'k'),
        'w': mots_avec(ens_mots, 'w'),
        'z': mots_avec(ens_mots, 'z')
    }
    
    # 2. Vérifier la présence de mots spécifiques
    mots_a_chercher = ["chronophage", "procrastinateur", "dangerosité", 
                      "gratifiant"]
    mots_trouves = [mot for mot in mots_a_chercher if mot in ens_mots]
    print("Mots recherchés présents dans le corpus :")
    print(mots_trouves, "\n")

    # 3. Mots de 7 lettres
    m7 = mots_de_n_lettres(ens_mots, 7)
    print(f"Nombre de mots de 7 lettres : {len(m7)}")
    print("Exemples :", random.sample(list(m7), min(5, len(m7))), "\n")

    # 4 à 6. Mots contenant 'k', 'w', 'z'
    print(f"Nombre de mots contenant 'k' : {len(mots_lettres['k'])}")
    print("Exemples :", random.sample(list(mots_lettres['k']), 
                                     min(5, len(mots_lettres['k']))), "\n")
    print(f"Nombre de mots contenant 'w' : {len(mots_lettres['w'])}")
    print("Exemples :", random.sample(list(mots_lettres['w']), 
                                     min(5, len(mots_lettres['w']))), "\n")
    print(f"Nombre de mots contenant 'z' : {len(mots_lettres['z'])}\n")

    # 7. Mots de 7 lettres contenant 'k'
    m7k = m7 & mots_lettres['k']
    print(f"Nombre de mots de 7 lettres contenant 'k' : {len(m7k)}\n")

    # 8. Mots contenant 'k' ET 'w'
    mkw = mots_lettres['k'] & mots_lettres['w']
    print(f"Nombre de mots contenant 'k' ET 'w' : {len(mkw)}\n")
    
    # 9. Mots commençant par 'z'
    m_z = {mot for mot in mots_lettres['z'] if mot.startswith('z')}
    print(f"Nombre de mots commençant par 'z' : {len(m_z)}\n")

    # 10. Mots terminant par 'z'
    mz_ = {mot for mot in mots_lettres['z'] if mot.endswith('z')}
    print(f"Nombre de mots terminant par 'z' : {len(mz_)}\n")

    # 11. Mots avec 'z' en position non terminale
    mznt = mots_lettres['z'] - m_z - mz_
    print(f"Nombre de mots avec 'z' en position non terminale : {len(mznt)}\n")

    # 12. Mots commençant par 'k'
    m_k = {mot for mot in mots_lettres['k'] if mot.startswith('k')}
    print(f"Nombre de mots commençant par 'k' : {len(m_k)}\n")

    # 13. Mots terminant par 'k'
    mk_ = {mot for mot in mots_lettres['k'] if mot.endswith('k')}
    print(f"Nombre de mots terminant par 'k' : {len(mk_)}\n")

    # 14. Mots avec 'k' en position non terminale
    mknt = mots_lettres['k'] - m_k - mk_
    print(f"Nombre de mots avec 'k' en position non terminale : {len(mknt)}\n")

    # 15. Mots avec 'k' en position non terminale ET 'z'
    print(f"Mots avec 'k' en position non terminale ET 'z' : {len(mknt & mots_lettres['z'])}\n")

if __name__ == "__main__":
    main()

# def main():
#     mots = liste_mots(FILENAME)
    
#     print( [ mots[i] for i in [24499, 28281, 57305, 118091, 199316, 223435, 336455] ])
#     # ['bachi-bouzouks', 'bayadères', 'coloquintes', 'ectoplasmes', 'macchabées', 'oryctéropes', 'zouaves']
    
#     print([ mot for mot in ["chronophage", "procrastinateur", "dangerosité", "gratifiant"] if mot in mots ])
#     # ['dangerosité', 'gratifiant']
    
#     m7 = mots_de_n_lettres(mots, 7)
#     print(len(m7))
#     # # 27945 mots de 7 lettres
#     print( random.sample(list(m7), 5))

#     mk = mots_avec(mots, 'k')
#     print(len(mk))
#     # # 1621 mots contenant un k
#     print( random.sample(list(mk), 5))

#     m7k = m7 & mk
#     print(len(m7k))
#     # 180 mots de 7 lettres contenant un k

#     mw = mots_avec(mots, 'w')
#     mkw = mk & mw
#     print(len(mkw))
#     # 32 mots contenant un k ET un w

#     mz = mots_avec(mots, 'z')
#     print(len(mz))
#     # 35177 mots contenant un z

#     m_z = { mot for mot in mz if mot.startswith('z')}
#     print(len(m_z))    
#     # 796 mots commençant par z

#     mz_ = { mot for mot in mz if mot.endswith('z')}
#     print(len(mz_))    
#     # 33118 mots terminant par z

#     mznt = mz - m_z - mz_
#     print(len(mznt))
#     # print()
#     # # 1330 mots avec z en position non terminale

#     print(m_z & mz_)

#     print(mznt&mk)

#     m_k = { mot for mot in mk if mot.startswith('k')}
#     print(len(m_k))    
#     # 491 mots commençant par k

#     mk_ = { mot for mot in mk if mot.endswith('k')}
#     print(len(mk_))    
#     # 84 mots terminant par k

#     mknt = mk - m_k - mk_
#     print(len(mknt))
#     # print()
#     # 1052 mots avec k en position non terminale

#     print(mknt&mz)


# if __name__ == "__main__":
#     main()
    



