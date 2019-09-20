import sys
sys.path.insert(0, 'C:/Users/trann/workspace/courselib')
import goody

def convert_to_dict(promptMessage: str) -> dict:
    """Prompts the user for a file name in the current directory.

    The file's information should be separated by whitespace with the
    information being first name, last name (suffix removed), team,
    all rank, sean rank, chris rank, and matthew rank.

    Returns: Dict | {Name: Sean rank}
    """

    errorMessage = 'Document does not exist'    
    open_file = goody.safe_open(promptMessage, 'r', errorMessage)

    playerRankings = {}
    
    for line in open_file:

        #unpack only important imformation
        split_info = line.split()

        #if they have suffix
        if len(split_info) == 8:
            firstName, lastName, suffix, _, _, SR, _, _ = split_info
            playerRankings[firstName + ' ' + lastName
                           + ' ' + suffix] = int(SR)
        else:
            firstName, lastName, _, _, SR, _, _ = line.split()
            playerRankings[firstName + ' ' + lastName] = int(SR)
    
    open_file.close()
    return playerRankings

def get_expert_ranks(promptMessage: str) -> dict:
    """Prompts the user for a file name in the current directory.

    The file's information should be separated by whitespace with the
    information being expert rank, first name, last name, and
    an optional suffix.

    Returns: Dict | {Name: expert rank}
    """

    errorMessage = 'Document does not exist'    
    open_file = goody.safe_open(promptMessage, 'r', errorMessage)

    expertRankings = {}
    
    for line in open_file:

        #unpack only important imformation
        split_info = line.split()

        #if they have suffix
        if len(split_info) == 4:
            rank, firstName, lastName, suffix = split_info
            expertRankings[firstName + ' ' + lastName
                           + ' ' + suffix] = int(rank)
        else:
            rank, firstName, lastName = line.split()
            expertRankings[firstName + ' ' + lastName] = int(rank)
    
    open_file.close()
    return expertRankings


def get_average(standardDict: dict, pprDict: dict) -> None:
    """Given two dictionaries, checks the rank for the same player
    and averages them

    After averaging the values, writes data to a new file"""

    for name, rank in standardDict.items():
        if name not in pprDict:
            pprDict[name + " Standard R"] = rank
        else:
            pprDict[name] = (pprDict[name] + rank)/2

    with open("averagedRanks.txt", "w") as end_file:
        for name in sorted(pprDict, key = lambda x: pprDict[x]):
            end_file.write("{name} {rank}\n".format(
                name = name, rank = pprDict[name]))

if __name__ == '__main__':

    
    get_average(convert_to_dict("Enter standard document"),
                convert_to_dict("Enter ppr document"))
