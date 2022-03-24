// Home Screen Date Header Component
import React from 'react'
import { StyleSheet, View, Text } from 'react-native'

// Current Date
const currentDate=()=>{
    var date = new Date().getDate();
    var month = new Date().getMonth();
    var year = new Date().getFullYear();
    return month + '/' + date + '/' + year;
}

// Date Header Component
export default function DateHeader() {
    return(
        <View style={styles.container}>
            <Text style={styles.dateText}>Today: {currentDate()}</Text>
        </View>
    )
}

// Date Header Style
const styles = StyleSheet.create({
    container: {
        marginVertical: 15,
        marginHorizontal: 20,
    },
    dateText: {
        color: '#99a29b',
        textAlign: 'left',
        fontSize: 18,
        fontWeight: 'bold'
    },
}) 