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
            <div>
                <h2>Race: {this.state.items.race}</h2>
                <h2>Class: {this.state.items._class}</h2>
                <h2>React ID: {this.state.items.id}</h2>
                <h2>Django_asdfadsfID: {this.props.id}</h2>
                <h2>TEST</h2>
            </div>
        )
    }
}
ReactDOM.render(
    React.createElement(Character, window.props),
    window.react_mount,
)