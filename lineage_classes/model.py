from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext

db = SQLAlchemy()

class L2_classes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    classess = db.Column(db.String(30), index = True, unique = True)
    archers = db.relationship('Archers', backref = 'l2_classes', lazy = 'dynamic')
    warriors = db.relationship('Warriors', backref = 'l2_classes', lazy = 'dynamic')
    mages = db.relationship('Mages', backref = 'l2_classes', lazy = 'dynamic')
    assassins = db.relationship('Assassins', backref = 'l2_classes', lazy = 'dynamic')

    def __repr__(self):
        return f'Class {self.classess}'


class Archers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Archer class {self.name} main role {self.role}'


class Warriors(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Warrior class {self.name} main role {self.role}'


class Mages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Mage class {self.name} main role {self.role}'


class Assassins(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)
    l2_classes_id = db.Column(db.Integer, db.ForeignKey('l2_classes.id'))

    def __repr__(self):
        return f'Assassin class {self.name} main role {self.role}'
    
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    archers = L2_classes(classess = 'Archers')

    warriors = L2_classes(classess = 'Warriors')

    mages = L2_classes(classess = 'Mages')

    assassins = L2_classes(classess = 'Assassins')

    db.session.add(archers)
    db.session.add(warriors)
    db.session.add(mages)
    db.session.add(assassins)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
        

    elven_archer = Archers(name = 'Elven Archer', race = 'Elf', armor = 'Light Armor', weapon = 'Bow', role = 'Deal Damage', description = '''The Silver Ranger is the ideal Elven fighter in terms of skill with the bow.
                        A Silver Ranger's key skills are Double Shot, which shoots two arrows consecutively, 
                        and Burst Shot, which hits multiple enemies within range.''', l2_classes_id = archers.id)

    human_archer = Archers(name = 'Human Archer', race = 'Human', armor = 'Light Armor', weapon = 'Bow', role = 'Deal Damage', description = '''Rather than using daggers, the Hawkeye threatens opponents from afar
                        using a longbow. Hawkeyes become even more powerful as part of a party. 
                        The Hawkeye's aim is accurate against single opponents, and a Hawkeye can also
                        attack groups of enemies effectively with skills such as Burst Shot.''', l2_classes_id = archers.id)

    dark_archer = Archers(name = 'Dark Elf Archer', race = 'Dark Elf', armor = 'Light Armor', weapon = 'Bow', role = 'Deal Damage', description = '''The Phantom Ranger handles a bow skillfully and uses techniques similar to those
                    of other Archers, but Phantom Rangers also have excellent attack strength.
                    By weakening the defensive strength of an opponent through Hex,
                    the Phantom Ranger can harass adversaries at long distances using Double Shot,
                    which shoots two arrows consecutively.''', l2_classes_id = archers.id)

    db.session.add(elven_archer)
    db.session.add(human_archer)
    db.session.add(dark_archer)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()

    warlord = Warriors(name = 'Warlord', race = 'Human', armor = 'Light or Heavy Armor', weapon = 'Spear', role = 'Attack', description = '''The Warlord is more capable in one-on-many battles 
                than in one-on-one combat and prefers long-range weapons, 
                such as poles. He casts gusts of thunderstorms that cause enemies to faint in their tracks. 
                The Warlord demonstrates his power most effectively in groups, such as during siege battles.''',l2_classes_id = warriors.id)

    gladiator = Warriors(name = 'Gladiator', race = 'Human', armor = 'Light or Heavy Armor', weapon = 'Dual Swords', role = 'Attack or Defence', description = '''None is better at one-on-one close combat than the Gladiator. 
                    Enemies attempt to avoid his powerful attacks in vain. The Gladiator displays his superior 
                    swordsmanship using the Sonic Storm or with two-bladed swords he implements the Triple Slash.''', l2_classes_id = warriors.id)

    sword_singer = Warriors(name = 'Sword Singer', race = 'Elf', armor = 'Heavy Armor', weapon = 'Swords or Blunts', role = 'Support', description = '''The Sword Singer has a beautiful voice that is used to 
                    raise the morale of party members and assist them in battle. The Sword Singer helps to recover 
                    the physical strength of party members through Song of Life and raises the defensive power 
                    of party members using Song of Earth. The sound of the Sword Singer's voice is welcome in any party.''', l2_classes_id = warriors.id)

    bladedancer = Warriors(name = 'Bladedancer', race = 'Dark Elf', armor = 'Heavy Armor', weapon = 'Dual Swords', role = 'Support', description = '''The Bladedancer primarily uses dual swords and raises the abilities 
                    of party members by dancing. They assist in the hunt by increasing the attack power 
                    of party members through the Dance of Warrior. The Bladedancer also raises the critical damage 
                    of party members through Dance of Fire.''', l2_classes_id = warriors.id)

    db.session.add(warlord)
    db.session.add(gladiator)
    db.session.add(sword_singer)
    db.session.add(bladedancer)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()


    treasure_hunter = Assassins(name = 'Treasure Hunter', race = 'Human', armor = 'Light Armor', weapon = 'Daggers', role = 'Attack', description = '''Treasure Hunters, known as the danger that lurks in the darkness,
                        act according to their own private goals. They move without fear or noise 
                        and backstab their enemies to eliminate them from behind.''', l2_classes_id = assassins.id)

    plains_walker = Assassins(name = 'Plains Walker', race = 'Elf', armor = 'Light Armor', weapon = 'Dagger', role = 'Attack', description = '''The Plains Walker, who is more accustomed to outdoor life 
                        than indoor living, is an adventurer skilled in all areas of battle and exploration. 
                        He attacks opponents from behind using Backstab and can entice one unique monster 
                        to benefit his party by using Lure.''', l2_classes_id = assassins.id)

    abyss_walker = Assassins(name = 'Abyss Walker', race = 'Dark Elf', armor = 'Light Armor', weapon = 'Daggers', role = 'Attack', description = '''The Abyss Walker is skilled in combat and exploration, 
                        specializing in assassinations. He implements the same basic techniques as the Human Mercenary 
                        with Silent Move and Backstab, but he has higher attack power. 
                        However, due to his relatively low physical strength, the Abyss Walker is at somewhat of a disadvantage 
                        in frontal battle.''', l2_classes_id = assassins.id)

    db.session.add(treasure_hunter)
    db.session.add(plains_walker)
    db.session.add(abyss_walker)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback()


    sorcerer = Mages(name = 'Sorcerer', race = 'Human', armor = 'Robe', weapon = 'Magic Weapon', role = 'Attack', description = '''The Sorcerer is a very perplexing being who borrows the power of the elements 
                to cast extreme elemental magic. He supports his allies by pouring fire down upon enemies 
                from a distance using Blazing Circle. Enemies within the Sorcerer's range are knocked 
                unconscious with Sleeping Cloud.''', l2_classes_id = mages.id)

    necromancer = Mages(name = 'Necromancer', race = 'Human', armor = 'Robe', weapon = 'Magic Weapon', role = 'Attack', description = '''The Necromancer makes use of the power of darkness 
                    by reviving the black magic of the titans. He summons zombies from corpses with Summon Zombie 
                    and causes great harm to his enemies through Corpse Burst.''', l2_classes_id = mages.id)

    spellsinger = Mages(name = 'SpellSinger', race = 'Elf', armor = 'Robe', weapon = 'Magic Weapon', role = 'Attack', description = '''The Spellsinger has become intimately familiar 
                    with elemental magic and deals in magic that primarily uses water. He uses a shield 
                    called Freezing Skin that reflects damage directed towards him and uses the Ice Dagger 
                    to throw ice blades at his opponents.''', l2_classes_id = mages.id)

    spellhowler = Mages(name = 'SpellHowler', race = 'Dark Elf', armor = 'Robes', weapon = 'Magic Weapon', role = 'Attack', description = '''The Spellhowler uses the highest degree of elemental magic.
                    A mix of Sorcerer and Necromancer, he casts magic by borrowing the power of the wind. 
                    The Spellhowler causes strong damage with the Tempest, which creates a tornado around his target, 
                    or he can use the Hurricane to shoot blades of wind from a distance.''', l2_classes_id = mages.id)

    db.session.add(sorcerer)
    db.session.add(necromancer)
    db.session.add(spellsinger)
    db.session.add(spellhowler)

    try:
        db.session.commit()
    except Exception:
        db.session.rollback
    click.echo('Initialized the database.')    