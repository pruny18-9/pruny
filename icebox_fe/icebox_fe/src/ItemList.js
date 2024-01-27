import './ItemList.css';

import React, { Component } from "react";
import axios from "axios";

// const BASE_URL = "http://localhost:5000"
const BASE_URL = "https://pruny.shop"

var Now = new Date();

class ItemList extends Component{
    constructor(props){
        super(props)

        this.state={
            items:[]
        }
    }

    fetchItems = () => {
        axios
            .get(BASE_URL + '/icebox/getItemList')
            .then(response => {
                console.log(response.data.data.length);
                console.log(response.data.data);
                this.setState({ items: response.data.data });
            })
            .catch(error => {
                console.log(error)
            })
    }

    componentDidMount(){
        this.fetchItems();
    }

    itemDelete = (item_id) => {
        axios
        .delete(BASE_URL + '/icebox/'+ item_id)
        .then(response=>{
          console.log(response.data.data);
          this.fetchItems();
        })
        .catch(error=>{
            console.log(error)
        })
            }

    render(){
        const {items} = this.state
        
        return (
            <div className="ItemList">
                {
                    items.length ?
                    items.map(item => 
                        <div className="Item" key={item.id}>
                            <button className='ItemDelete' onClick={() => this.itemDelete(item.id)}>❌</button>
                            <img className="ItemImg" src={item.img}/>
                            <div className='ItemText'>
                                <p className='ItemName'>{item.name}</p>
                                <p className='ItemDate'>{parseInt((Now - Date.parse(item.regdate))/(24*60*60*1000))}일 지남</p>
                            </div>
                            {/* <li>
                                {item.expdate}
                            </li> */}
                        </div>):
                    null
                }
                
            </div>       
        )
    }
}



export default ItemList