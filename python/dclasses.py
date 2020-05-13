from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

idef main():
    card = DataClassCard('Q', 'Hearts')
    print("it ran")


if __name__ == '__main__':
    main()
