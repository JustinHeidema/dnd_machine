var React = require('react')
var ReactDOM = require('react-dom')
import DjangoCSRFToken from 'django-react-csrftoken'

export default class Main extends React.Component {
    constructor() 
    {
        super();
        this.fetchDwarf = this.fetchDwarf.bind(this);
        this.fetchElf = this.fetchElf.bind(this);
        this.fetchHalfling = this.fetchHalfling.bind(this);
        this.fetchHuman = this.fetchHuman.bind(this);
        this.fetchDragonborn = this.fetchDragonborn.bind(this);
        this.fetchGnome = this.fetchGnome.bind(this);
        this.fetchHalfElf = this.fetchHalfElf.bind(this);
        this.fetchHalfOrc = this.fetchHalfOrc.bind(this);
        this.fetchTiefling = this.fetchTiefling.bind(this);

        this.fetchBarbarian = this.fetchBarbarian.bind(this);
        this.fetchBard = this.fetchBard.bind(this);
        this.fetchCleric = this.fetchCleric.bind(this);
        this.fetchDruid = this.fetchDruid.bind(this);
        this.fetchFighter = this.fetchFighter.bind(this);
        this.fetchMonk = this.fetchMonk.bind(this);
        this.fetchPaladin = this.fetchPaladin.bind(this);
        this.fetchRanger = this.fetchRanger.bind(this);
        this.fetchRogue = this.fetchRogue.bind(this);
        this.fetchSorcerer = this.fetchSorcerer.bind(this);
        this.fetchWarlock = this.fetchWarlock.bind(this);
        this.fetchWizard = this.fetchWizard.bind(this);
        this.state = 
        { 
        	race_items: 
        	{
        		race_name: "",
        		strength_modifier: 0,
        		dexterity_modifier: 0,
        		constitution_modifier: 0,
        		intelligence_modifier: 0,
        		wisdom_modifier: 0,
        		charisma_modifier: 0,
        		speed: 0,
        		languages: [],
        		race_traits:
        		[
        		    {
        		        trait_name: "",
        		        trait_effect: "",
        		    }
        		],
        	},
            class_items:
            {
                class_name: "",
                hit_die: 0,
                skills: [],
                from_skills_choose: 0,
                proficiencies: [
                    {
                        proficiency: "",
                        proficiency_type: "",
                    }
                ],
                saving_throws: [
                    {
                        short_name: "",
                        long_name: "",
                    }
                ],
            }

    	};
    }

    fetchDwarf(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/dwarf/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchElf(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/elf/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchHalfling(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/halfling/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchHuman(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/human/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchDragonborn(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/dragonborn/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchGnome(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/gnome/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchHalfElf(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/halfelf/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchHalfOrc(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/halforc/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchTiefling(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/races/tiefling/').then(result=> {
            result.json().then(data=> {
                this.setState({race_items:data})
            });
       });
    }

    fetchBarbarian(e) 
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/barbarian').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchBard(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/bard').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchCleric(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/cleric').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchDruid(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/druid').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchFighter(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/fighter').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchMonk(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/monk').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchPaladin(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/paladin').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchRanger(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/ranger').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchRogue(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/rogue').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchSorcerer(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/sorcerer').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchWarlock(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/warlock').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }

    fetchWizard(e)
    {
       e.preventDefault();
       fetch('http://localhost:8000/character_builder/api/classes/wizard').then(result=> {
            result.json().then(data=> {
                this.setState({class_items:data})
            });
       });
    }


    render () 
    {
        return (
            <div>
                <div id='race_info'>
                    <div id='race_buttons'>
                        <h1>Race</h1>
                        <form name='fetchDwarf' onSubmit={this.fetchDwarf}>
                            <button className='race_button'>Dwarf</button>
                        </form>
                        <form name='fetchElf' onSubmit={this.fetchElf}>
                            <button className='race_button'>Elf</button>
                        </form>
                        <form name='fetchHalfling' onSubmit={this.fetchHalfling}>
                            <button className='race_button'>Halfling</button>
                        </form>
                        <form name='fetchHuman' onSubmit={this.fetchHuman}>
                            <button className='race_button'>Human</button>
                        </form>
                        <form name='fetchDragonborn' onSubmit={this.fetchDragonborn}>
                            <button className='race_button'>Dragonborn</button>
                        </form>
                        <form name='fetchGnome' onSubmit={this.fetchGnome}>
                            <button className='race_button'>Gnome</button>
                        </form>
                        <form name='fetchHalfElf' onSubmit={this.fetchHalfElf}>
                            <button className='race_button'>Half Elf</button>
                        </form>
                        <form name='fetchHalfOrc' onSubmit={this.fetchHalfOrc}>
                            <button className='race_button'>Half Orc</button>
                        </form>
                        <form name='fetchTiefling' onSubmit={this.fetchTiefling}>
                            <button className='race_button'>Tiefling</button>
                        </form>
                    </div>
                    <div id='race_stats'>
                        <h1>{this.state.race_items.race_name}</h1>
                        <p>Strength Modifier: {this.state.race_items.strength_modifier}</p>
                        <p>Dexterity Modifier: {this.state.race_items.dexterity_modifier}</p>
                        <p>Constitution Modifier: {this.state.race_items.constitution_modifier}</p>
                        <p>Intelligence Modifier: {this.state.race_items.intelligence_modifier}</p>
                        <p>Wisdom Modifier: {this.state.race_items.wisdom_modifier}</p>
                        <p>Charisma Modifier: {this.state.race_items.charisma_modifier}</p>

                        <h3>Languages</h3>
                        {
                            this.state.race_items.languages.map((language) =>
                                {return <p key={language.toString()}>{language}</p>})
                        }

                        <h3>Race Traits</h3>
                        {
                            this.state.race_items.race_traits.map((race_trait) =>
                                {return <div key={race_trait.toString()}>
                                    <h4 key={race_trait['trait_name'].toString()}>{race_trait['trait_name']}</h4>
                                    <p key={race_trait['trait_effect'].toString()}>{race_trait['trait_effect']}</p>
                                    </div>
                                })
                        }
                    </div>
                </div>
                <div id='class_info'>
                    <div id='class_buttons'>
                        <h1>Class</h1>
                        <form name='fetchBarbarian' onSubmit={this.fetchBarbarian}>
                            <button className='class_button'>Barbarian</button>
                        </form>
                        <form name='Bard' onSubmit={this.fetchBard}>
                            <button className='class_button'>Bard</button>
                        </form>
                        <form name='fetchCleric' onSubmit={this.fetchCleric}>
                            <button className='class_button'>Cleric</button>
                        </form>
                        <form name='fetchDruid' onSubmit={this.fetchDruid}>
                            <button className='class_button'>Druid</button>
                        </form>
                        <form name='fetchFighter' onSubmit={this.fetchFighter}>
                            <button className='class_button'>Fighter</button>
                        </form>
                        <form name='fetchMonk' onSubmit={this.fetchMonk}>
                            <button className='class_button'>Monk</button>
                        </form>
                        <form name='fetchPaladin' onSubmit={this.fetchPaladin}>
                            <button className='class_button'>Paladin</button>
                        </form>
                        <form name='fetchRanger' onSubmit={this.fetchRanger}>
                            <button className='class_button'>Ranger</button>
                        </form>
                        <form name='fetchRogue' onSubmit={this.fetchRogue}>
                            <button className='class_button'>Rogue</button>
                        </form>
                        <form name='fetchSorcerer' onSubmit={this.fetchSorcerer}>
                            <button className='class_button'>Sorcerer</button>
                        </form>
                        <form name='fetchWarlock' onSubmit={this.fetchWarlock}>
                            <button className='class_button'>Warlock</button>
                        </form>
                        <form name='fetchWizard' onSubmit={this.fetchWizard}>
                            <button className='class_button'>Wizard</button>
                        </form>
                    </div>
                    <div>
                        <h1>{ this.state.class_items.class_name } </h1>
                        <h3>Hit Dice: { this.state.class_items.hit_die }</h3>
                        <h3>Skills</h3>
                        <p><b>From </b></p> <p>{
                                        this.state.class_items.skills.map((result) =>
                                            {return <span key={result.toString()}>{result}, </span>})
                                      }</p>
                        <p><b>Choose</b> {this.state.class_items.from_skills_choose} </p>
                        <h3>Proficiencies</h3>
                        <p>{
                            this.state.class_items.proficiencies.map((result) =>
                                {return <span key={result['proficiency'].toString()}>{result['proficiency']}, </span>})
                        }</p>
                        <h3>Saving Throws</h3>
                        {
                            this.state.class_items.saving_throws.map((result) =>
                                {return <p key={result['long_name'].toString()}>{result['long_name']}</p>})
                        }
                    </div>
                </div>
                <div id='character_choices'>
                    <h1>Select your Ability Scores</h1>
                    <table>
                        <tbody>
                            <tr>
                                <th>Strength</th>
                                <th>Dexterity</th>
                                <th>Constitution</th>
                                <th>Intelligence</th>
                                <th>Wisdom</th>
                                <th>Charisma</th>
                            </tr>
                            <tr>
                                <td><input type='text' name='strength' /></td>
                                <td><input type='text' name='dexterity' /></td>
                                <td><input type='text' name='constitution' /></td>
                                <td><input type='text' name='intelligence' /></td>
                                <td><input type='text' name='wisdom' /></td>
                                <td><input type='text' name='charisma' /></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
}

ReactDOM.render(
  <Main />,
  document.getElementById('container')
);