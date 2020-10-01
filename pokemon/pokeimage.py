import wget

def wget_pic(imagelink):
    # code goes here!
    # image must be saved to /home/student/mycode
    
    wget.download(imagelink, f'/home/student/mycode/pokemon.png')


def main():
    url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png'
    wget_pic(url)

main()
