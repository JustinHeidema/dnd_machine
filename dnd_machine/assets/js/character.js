var React = require('react')
var ReactDOM = require('react-dom')
import DjangoCSRFToken from 'django-react-csrftoken'

export default class Character extends React.Component
{
    constructor()
    {
        super();
        this.state =
        {
            items:
            {
                id: 0,
                race: "test_race",
                _class: "test_class",
                strength: 0,
                dexterity: 0,
                constitution: 0,
                intelligence: 0,
                wisdom: 0,
                charisma: 0,
                speed: 0,
                hit_die: 0,
                skill_array: [],
                language_array: [],
                race_traits:
                [
                    {
                        trait_name: "",
                        trait_effect: "",
                    }
                ]
            }
        }
    }

    fetchCharacter(e)
    {
        e.preventDefault();
        fetch('http://localhost:8000/character_builder/api/characters/' + this.state.items.id).then(result=> {
            result.json().then(data=> {
               this.setState({items:data})
            });
        });
    }

    render()
    {
        return (
            <div id='character_review'>
                <h1>{this.props.name}</h1>
                <h2>Race: {this.props.race}</h2>
                <h2>Class: {this.props._class}</h2>
                <h2>ID: {this.props.id}</h2>
                <p>Strength: {this.props.strength}</p>
                <p>Dexterity: {this.props.dexterity}</p>
                <p>Constitution: {this.props.constitution}</p>
                <p>Intelligence: {this.props.intelligence}</p>
                <p>Wisdom: {this.props.wisdom}</p>
                <p>Charisma: {this.props.charisma}</p>
                <h2>Skills</h2>
                {this.props.skill_array.map((skill) =>
                    {return <p key={skill}>{skill}</p>}
                )}
                <h2>Languages</h2>
                {this.props.language_array.map((language) =>
                    {return <p key={language}>{language}</p>}
                )}
                <h2>Race Traits</h2>
                {
                    this.props.race_traits.map((race_trait) =>
                        {return <div>
                            <h4 key={race_trait['trait_name']}>{race_trait['trait_name']}</h4>
                            <p key={race_trait['trait_effect']}>{race_trait['trait_effect']}</p>
                            </div>
                        })
                }

            </div>
        )
    }
}
ReactDOM.render(
    React.createElement(Character, window.props),
    window.react_mount,
)