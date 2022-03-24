// Team Screen Scheduled Members Component
import React from 'react'
import { View, FlatList, StyleSheet, Text } from 'react-native'

/* example data to use for scroll 
    - need to connect to database to retrieve users:
        not scheduled
        scheduled
            clocked in/out - 
            
    - connection to mySQL needed**
*/
const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First Name',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Name',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Name',
  },
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First Name',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Name',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Name',
  },{
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First Name',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Name',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Name',
  },{
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'First Name',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Second Name',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Third Name',
  },
];

// List Item 
const Item = ({ title }) => (
  <View style={styles.item}>

    <View style={styles.itemLayout}>
      <Text style={styles.nameText}>{title}</Text>
      <View style={styles.statusIndicator}></View>
    </View>

    <View style={styles.listLines}></View>

  </View>
);

// Scheduled Component
export default function ScheduledTeam() {
  const renderItem = ({ item }) => (
    <Item title={item.title} />
  );
  return (
    // Container 
    <View style={styles.container}>

      <View>
        <Text style={styles.scheduledText}>SCHEDULED</Text>
        <View style={styles.line}></View>
      </View>

      <FlatList
        style={styles.list}
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item.id}
      />

    </View>
  )
}

// Schedule Team Component Style
const styles = StyleSheet.create({
    container: {
      backgroundColor: 'white',
      width: '90%',
      height: '42%',
      borderRadius: 10,
      marginLeft: 20,
      marginRight: 20,
      marginTop: 20,
      shadowOpacity: .30,
      shadowRadius: 2,
      shadowOffset: {height: 0, width: 1},
    },
    scheduledText: {
      color: '#b0b7b1',
      textAlign: 'center',
      paddingTop: 15,
      paddingBottom: 15,
      fontSize: 28,
      fontWeight: '700',
    },
    line: {
      borderBottomColor: '#b0b7b1',
      borderBottomWidth: 1,
      marginLeft: 20,
      marginRight: 20,
    },
    list: {
      marginTop: 15,
    },
    item: {
      marginLeft: 20,
    },
    itemLayout: {
      flexDirection: 'row',
      justifyContent: 'space-between',
    },
    nameText: {
      color: '#89938a',
      fontSize: 14,
      fontWeight: '600',
    },
    statusIndicator: {
      backgroundColor: '#2ac725', // #2ac725 green color
      width: 15,
      height: 15,
      borderColor: '#99a29b',
      borderRadius: 50,
      borderWidth: 1,
      marginRight: 20,
  },
    listLines: {
      borderBottomColor: '#b0b7b1',
      borderBottomWidth: 1,
      marginVertical: 15,
      marginRight: 20,
    },
})