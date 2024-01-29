import './ItemList.css';
import ItemCreateView from'./ItemCreateView.js';
import React, { Component } from "react";
import axios from "axios";

// const BASE_URL = "http://localhost:5000"
const BASE_URL = "https://pruny.shop"

var Now = new Date();


class ItemList extends Component{
    constructor(props){
        super(props)

        this.state={
            items:[],
            item_create_view:false
        }
    }

    componentDidMount(){
        this.fetchItems();
    }

    fetchItems = () => {
        axios
            .get(BASE_URL + '/icebox/getItemList')
            .then(response => {
                // console.log(response.data.data.length);
                // console.log(response.data.data);
                this.setState({ items: response.data.data });
            })
            .catch(error => {
                console.log(error)
            })
    }

    itemCreateView = () => {
        this.setState({
            item_create_view: this.state.item_create_view? false:true
        })
    }

    itemCreate = (item_name, item_img) => {
        axios
        .post(BASE_URL + '/icebox/registItem', {
            "name": item_name,
            "img": item_img
        })
        .then(response=>{
            console.log(response.data.data);
            this.fetchItems();
        })
        .catch(error=>{
            console.log(error)
        })             
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
            <div >
                {this.state.item_create_view && <ItemCreateView itemCreate={this.itemCreate}/>}
                <button className='ItemCreate' onClick={()=>this.itemCreateView()}>+</button>
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
                        </div>):
                    null
                } </div>
                               
            </div>                   
        )
    }
}



export default ItemList