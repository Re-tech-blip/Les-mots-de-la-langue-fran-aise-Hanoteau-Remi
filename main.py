#### Imports et définition des variables globales

import random

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires

def read_data(filename):
    """
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
    >>> mots[233574]
    'péril'
    >>> mots[221712]
    'on'
    >>> mots[324539]
    'triomphe'
    >>> mots[290761]
    'sans'
    >>> mots[166128]
    'gloire'
    """
    with open(filename, "r", encoding="utf-8") as file:
        mots = file.read().split() 
    return mots


def ensemble_mots(filename):
    """retourne les mots contenus dans filename

    Args:
        filename (str): nom du fichier

    Returns:
        list: la liste des mots

    >>> mots = ensemble_mots(FILENAME)
    >>> isinstance(mots, set)
    True
    >>> len(mots)
    336531
    >>> "glomérules" in mots
    True
    >>> "glycosudrique" in mots
    False
    """
    
    return set(read_data(filename))

def mots_de_n_lettres(mots, n):
    """retourne le sous ensemble des mots de n lettres

    Args:
        mots (set): ensemble de mots
        n (int): nombre de lettres

    Returns:
        set: sous ensemble des mots de n lettres

    >>> mots = ensemble_mots(FILENAME)
    >>> m15 = mots_de_n_lettres(mots, 15)
    >>> isinstance(m15, set)
    True
    >>> len(m15)
    8730
    >>> list({ len(mots_de_n_lettres(mots,i)) for i in range(15,26)})
    [4418, 2, 4, 2120, 42, 11, 205, 977, 437, 8730, 94]
    >>> sorted(list(mots_de_n_lettres(mots,23)))[0]
    'constitutionnalisassent'
    >>> sorted(list(mots_de_n_lettres(mots,24)))
    ['constitutionnalisassions', 'constitutionnaliseraient', 'hospitalo-universitaires', 'oto-rhino-laryngologiste']
    >>> sorted(list(mots_de_n_lettres(mots,25)))
    ['anticonstitutionnellement', 'oto-rhino-laryngologistes']
    """
    l = ""
    return {mot for mot in mots if len(mot) == n}


def mots_avec(mots, s):
    """retourne le sous ensemble des mots incluant la lettre l

    Args:
        mots (set): ensemble de mots
        s (str): chaine de caractères à inclure

    Returns:
        set: sous ensemble des mots incluant la chaine de caractères s

    >>> mots = ensemble_mots(FILENAME)
    >>> mk = mots_avec(mots, 'k')
    >>> isinstance(mk, set)
    True
    >>> len(mk)
    1621
    >>> sorted(list(mk))[35:74:7]
    ['ankyloseraient', 'ankyloserons', 'ankylostome', 'ankylosée', 'ashkénaze', 'bachi-bouzouks']
    >>> sorted(list(mk))[147:359:38]
    ['black', 'blackboulèrent', 'cheikhs', 'cokéfierais', 'dock', 'dénickeliez']
    >>> sorted(list(mk))[999::122]
    ['képi', 'nickela', 'parkérisiez', 'semi-coke', 'stockais', 'week-end']
    """
    
    return {mot for mot in mots if s in mot}


def cherche1(mots, start, stop, n):
    """retourne le sous ensemble des mots de n lettres commençant par start et finissant par stop

    Args:
        mots (set): ensemble de mots
        start (str): première lettre
        stop (str): dernière lettre
        n (int): nombre de lettres

    Returns:
        set: sous ensemble des mots de n lettres commençant par start et finissant par stop

    >>> mots = ensemble_mots(FILENAME)
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


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    """effectue une recherche complexe dans un ensemble de mots

    Args:
        mots (set): ensemble de mots
        lstart (list): liste des préfixes
        lmid (list): liste des chaines de caractères intermédiaires
        lstop (list): liste des suffixes
        nmin (int): nombre de lettres minimum
        nmax (int): nombre de lettres maximum

    Returns:
        set: retourne le sous ensemble des mots commençant par une chaine présente dans lstart, contenant une chaine présente dans lmid et finissant par une chaine présente dans lstop, avec un nombre de lettres entre nmin et nmax

    >>> mots = ensemble_mots(FILENAME)
    >>> mab17ez = cherche2(mots, 'a', 'b', 'z', 16, 16)
    >>> isinstance(mab17ez, set)
    True
    >>> len(mab17ez)
    1
    >>> mab17ez
    {'alphabétisassiez'}
    """
    result = set()
    for mot in mots:
        # Vérifier la longueur
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


import random

# Variables globales
FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

def read_data(filename):
    """Lit un fichier et retourne une liste de mots."""
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip() != "" or line == "\n"]

def ensemble_mots(filename):
    """Retourne un ensemble de mots uniques."""
    return set(read_data(filename))

def mots_de_n_lettres(mots, n):
    """Retourne les mots de n lettres."""
    return {mot for mot in mots if len(mot) == n}

def mots_avec(mots, s):
    """Retourne les mots contenant la chaîne s."""
    return {mot for mot in mots if s in mot}

def cherche1(mots, start, stop, n):
    """Retourne les mots de n lettres commençant par start et finissant par stop."""
    return {
        mot for mot in mots
        if len(mot) == n
        and mot.startswith(start)
        and mot.endswith(stop)
    }

def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    """Recherche complexe de mots."""
    result = set()
    for mot in mots:
        if not (nmin <= len(mot) <= nmax):
            continue
        if (any(mot.startswith(prefix) for prefix in lstart) and
            any(mot.endswith(suffix) for suffix in lstop) and
            any(mid in mot for mid in lmid)):
            result.add(mot)
    return result

def main():
    """Fonction principale pour démontrer l'utilisation des fonctions."""
    # 1. Lire les données et créer l'ensemble de mots
    mots = read_data(FILENAME)
    ens = ensemble_mots(FILENAME)

    print("=== Analyse du corpus ===")
    print(f"Nombre total de mots : {len(mots)}")
    print(f"Nombre de mots uniques : {len(ens)}\n")

    # 2. Vérifier la présence de mots spécifiques
    mots_a_chercher = ["chronophage", "procrastinateur", "dangerosité", "gratifiant"]
    mots_trouves = [mot for mot in mots_a_chercher if mot in ens]
    print("Mots recherchés présents dans le corpus :")
    print(mots_trouves, "\n")

    # 3. Mots de 7 lettres
    m7 = mots_de_n_lettres(ens, 7)
    print(f"Nombre de mots de 7 lettres : {len(m7)}")
    print("Exemples :", random.sample(list(m7), min(5, len(m7))), "\n")

    # 4. Mots contenant 'k'
    mk = mots_avec(ens, 'k')
    print(f"Nombre de mots contenant 'k' : {len(mk)}")
    print("Exemples :", random.sample(list(mk), min(5, len(mk))), "\n")

    # 5. Mots contenant 'w'
    mw = mots_avec(ens, 'w')
    print(f"Nombre de mots contenant 'w' : {len(mw)}")
    print("Exemples :", random.sample(list(mw), min(5, len(mw))), "\n")

    # 6. Mots contenant 'z'
    mz = mots_avec(ens, 'z')
    print(f"Nombre de mots contenant 'z' : {len(mz)}\n")

    # 7. Mots de 7 lettres contenant 'k'
    m7k = m7 & mk
    print(f"Nombre de mots de 7 lettres contenant 'k' : {len(m7k)}\n")

    # 8. Mots contenant 'k' ET 'w'
    mkw = mk & mw
    print(f"Nombre de mots contenant 'k' ET 'w' : {len(mkw)}\n")

    # 9. Mots commençant par 'z'
    m_z = {mot for mot in mz if mot.startswith('z')}
    print(f"Nombre de mots commençant par 'z' : {len(m_z)}\n")

    # 10. Mots terminant par 'z'
    mz_ = {mot for mot in mz if mot.endswith('z')}
    print(f"Nombre de mots terminant par 'z' : {len(mz_)}\n")

    # 11. Mots avec 'z' en position non terminale
    mznt = mz - m_z - mz_
    print(f"Nombre de mots avec 'z' en position non terminale : {len(mznt)}\n")

    # 12. Mots commençant par 'k'
    m_k = {mot for mot in mk if mot.startswith('k')}
    print(f"Nombre de mots commençant par 'k' : {len(m_k)}\n")

    # 13. Mots terminant par 'k'
    mk_ = {mot for mot in mk if mot.endswith('k')}
    print(f"Nombre de mots terminant par 'k' : {len(mk_)}\n")

    # 14. Mots avec 'k' en position non terminale
    mknt = mk - m_k - mk_
    print(f"Nombre de mots avec 'k' en position non terminale : {len(mknt)}\n")

    # 15. Mots avec 'k' en position non terminale ET 'z'
    print(f"Mots avec 'k' en position non terminale ET 'z' : {len(mknt & mz)}\n")

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
    



